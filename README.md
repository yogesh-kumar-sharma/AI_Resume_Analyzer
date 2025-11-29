# 🧠 AI Resume Analyzer — Smart Resume Analysis Tool

<p align="center">
  <img src="https://github.com/yogesh-kumar-sharma/AI_Resume_Analyzer/assets/demo.gif" width="750" alt="AI Resume Analyzer Demo Animation"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue"/>
  <img src="https://img.shields.io/badge/Flask-Framework-green"/>
  <img src="https://img.shields.io/badge/NLP-Enabled-orange"/>
  <img src="https://img.shields.io/badge/AI-Resume%20Analysis-purple"/>
  <img src="https://img.shields.io/github/stars/yogesh-kumar-sharma/AI_Resume_Analyzer?style=social"/>
</p>

---

## 📘 Table of Contents

* [Overview](#-overview)
* [Features](#-features)
* [Tech Stack](#-tech-stack)
* [Project Structure](#-project-structure)
* [Installation](#️-installation)
* [Run the Application](#️-run-the-application)
* [Screenshots](#-screenshots)
* [Future Improvements](#-future-improvements)
* [Contributing](#-contributing)
* [License](#-license)

---

An intelligent and automated Resume Analysis Web Application built using **Python**, **Flask**, and **Natural Language Processing (NLP)**. This project evaluates resumes, extracts meaningful insights, compares them with job descriptions, and provides improvement suggestions.

---

## 🔍 Overview

A modern AI-powered web application that analyzes resumes using NLP techniques, compares them with job descriptions, and gives meaningful suggestions for improvement. Designed for job seekers, HR teams, and recruiters.
The **AI Resume Analyzer** helps job seekers understand how well their resume matches a given job description. It performs keyword extraction, skill matching, content scoring, and improvement suggestions.

The system uses:

* NLP-based text extraction & analysis
* Flask backend for file uploads and processing
* HTML/CSS for a simple frontend interface

---

## 🚀 Features

Here’s what the AI Resume Analyzer can do:

* **Resume Upload (PDF)**
* **Job Description Analyzer**
* **Keyword Matching**
* **Skill Extraction**
* **Content Score Calculation**
* **Suggestions for Resume Improvement**
* **Clean UI for Uploading and Viewing Results**

---

## 🧪 Tech Stack

**Backend:** Python, Flask
**Libraries:** nltk, re, PyPDF2, etc.
**Frontend:** HTML, CSS
**Version Control:** Git & GitHub

---

## 📁 Project Structure

```
AI_Resume_Analyzer/
│
├── app.py                  # Flask main application
├── utils.py                # NLP processing functions
├── templates/              # Frontend HTML templates
│   ├── index.html
│   └── result.html
├── static/                 # Static files (uploads, css, images)
│   └── uploads/
├── requirements.txt        # Python dependencies
└── .gitignore              # Ignored system & venv files
```

---

## 🛠️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yogesh-kumar-sharma/AI_Resume_Analyzer.git
cd AI_Resume_Analyzer
```

### 2️⃣ Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # Mac / Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Go to your browser and open:
👉 [http://127.0.0.1:5500](http://127.0.0.1:5500) or [http://localhost:5500](http://localhost:5500)

---

## 📸 Screenshots

You can update the following sections with actual screenshots:

* **Home Page (Upload Resume)**
* **Job Description Input Page**
* **Analysis Result Page**

Example Placeholder:
![App Screenshot Placeholder](https://via.placeholder.com/900x400?text=Add+Your+Screenshot+Here)
You can add screenshots of:

* Homepage
* Upload Page
* Output Result Page

---

## 🔮 Future Improvements

* Add machine learning model for scoring
* Provide resume formatting suggestions
* Add support for DOCX files
* Create downloadable detailed reports

---

## 🤝 Contributing

If you’d like to improve this project, feel free to fork the repo and submit a pull request.

Steps:

1. Fork the repo
2. Create a new branch (`feature-branch`)
3. Commit your changes
4. Push & create a PR
   Pull requests are welcome. For major changes, open an issue first.

---

## 📝 License

This project is open-source and can be used for learning, personal, or portfolio purposes.
This project is free for educational and personal use.

---

### ⭐ If you like this project, don't forget to star the repository!
