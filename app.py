from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import fitz
from sentence_transformers import SentenceTransformer, util
from utils import extract_entities
import re

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# -------------------------------
# Extract text from PDF
# -------------------------------
def extract_text_pymupdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    doc.close()
    return text.strip()


# -------------------------------
# AI-Style Resume Rewrite
# -------------------------------
def generate_ai_rewrite(resume_text, job_description, matched_skills):
    top_skills = ", ".join(matched_skills[:8]) if matched_skills else "relevant skills"
    jd_snippet = " ".join(job_description.split()[:35]) + "..." if job_description else ""

    summary = f"""
Rewrite this resume summary to better match the job description:

Target Role Context:
• {jd_snippet}

Recommended Summary:
"Result-driven professional skilled in {top_skills}, with strong ability to learn fast, collaborate effectively, and deliver impactful results. Adept at solving problems, improving systems, and contributing meaningfully to team success. Eager to bring value aligned with the job requirements."
    """
    return summary.strip()


# -------------------------------
# Detect Weak / Generic Resume Lines
# -------------------------------
def find_weak_lines(resume_text):
    weak_patterns = [
        "responsible for",
        "worked on",
        "involved in",
        "tasked with",
        "duties included",
        "helped with",
    ]

    lines = re.split(r"[\n\.]", resume_text)
    weak_lines = []

    for line in lines:
        cleaned = line.strip()
        if not cleaned:
            continue

        lower = cleaned.lower()
        if any(p in lower for p in weak_patterns) and not re.search(r"\d", cleaned):
            weak_lines.append(cleaned)

    return weak_lines


# -------------------------------
# Resume Score Calculation System
# -------------------------------
def calculate_resume_scores(resume_text, matched_skills, missing_skills):

    # Skill Match Score
    total_skills = len(matched_skills) + len(missing_skills)
    skill_match_score = int(100 * len(matched_skills) / total_skills) if total_skills > 0 else 50

    # Years of Experience
    years = []
    for yr in re.findall(r"(\d+)\+?\s*(?:years?|yrs?)", resume_text.lower()):
        try:
            years.append(int(yr))
        except:
            pass

    max_years = max(years) if years else 0
    if max_years >= 8:
        experience_score = 95
    elif max_years >= 5:
        experience_score = 85
    elif max_years >= 3:
        experience_score = 75
    elif max_years >= 1:
        experience_score = 65
    else:
        experience_score = 50

    # Formatting Score
    headings = ["experience", "work", "projects", "education", "skills", "summary"]
    heading_hits = sum(1 for h in headings if h in resume_text.lower())
    heading_score = int(100 * heading_hits / len(headings))

    bullet_score = 100 if any(x in resume_text for x in ["•", "-", "●"]) else 65

    word_count = len(resume_text.split())
    if word_count < 150:
        length_score = 55
    elif word_count < 350:
        length_score = 80
    elif word_count < 1000:
        length_score = 95
    else:
        length_score = 75

    formatting_score = int(0.5 * heading_score + 0.2 * bullet_score + 0.3 * length_score)

    # ATS Score
    ats_score = int(0.6 * skill_match_score + 0.4 * formatting_score)

    # Final overall
    overall_score = int(
        0.4 * skill_match_score
        + 0.3 * experience_score
        + 0.3 * formatting_score
    )

    return {
        "overall_score": overall_score,
        "skill_match_score": skill_match_score,
        "experience_score": experience_score,
        "formatting_score": formatting_score,
        "ats_score": ats_score,
    }


# -------------------------------
# Load AI Model
# -------------------------------
model = SentenceTransformer('stsb-roberta-large')


# -------------------------------
# Routes
# -------------------------------
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    resume_file = request.files["resume"]
    job_desc = request.form["job_description"]

    if not resume_file or not job_desc:
        return "Resume or Job Description missing.", 400

    filename = secure_filename(resume_file.filename)
    save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    resume_file.save(save_path)

    # Extract resume text
    resume_text = extract_text_pymupdf(save_path)

    # Similarity (Match Score)
    emb = model.encode([resume_text, job_desc], convert_to_tensor=True)
    match_score = round(float(util.pytorch_cos_sim(emb[0], emb[1]).item()) * 100, 2)

    # Skill extraction
    resume_entities = extract_entities(resume_text)
    resume_skills = set(s.lower() for s in resume_entities.get("SKILL", []))

    jd_words = set(re.findall(r"\b\w{4,}\b", job_desc.lower()))
    matched_skills = sorted(jd_words & resume_skills)
    missing_skills = sorted(jd_words - resume_skills)[:10]

    # Suggestions
    suggestions = []
    if "flask" in jd_words and "flask" not in resume_text.lower():
        suggestions.append("Add your Flask or backend experience.")
    if "sql" in jd_words and "sql" not in resume_text.lower():
        suggestions.append("Mention SQL or database exposure.")
    if "api" in jd_words and "api" not in resume_text.lower():
        suggestions.append("Add details of APIs you built or used.")
    if len(resume_text.split()) < 150:
        suggestions.append("Your resume is short. Add more details.")
    if not any(h in resume_text.lower() for h in ["experience", "projects", "work"]):
        suggestions.append("Add an 'Experience' or 'Projects' section.")

    # Score Breakdown System
    scores = calculate_resume_scores(resume_text, matched_skills, missing_skills)

    # AI Resume Rewrite
    improved_summary = generate_ai_rewrite(resume_text, job_desc, matched_skills)

    # Weak Lines
    weak_lines = find_weak_lines(resume_text)

    return render_template(
        "result.html",
        match_score=match_score,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        suggestions=suggestions,
        improved_summary=improved_summary,
        weak_lines=weak_lines,
        **scores,
    )


if __name__ == "__main__":
    app.run(debug=True)

print("AI Resume Analyzer — Developed by Yogesh Parshuram Sharma")

#source venv/bin/activate
# python3 app.py
