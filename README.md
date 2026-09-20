# Fake Job Posting Detection

A machine learning project that detects whether a job posting is likely to be **Real** or **Fake** using a Decision Tree Classifier.

## Project Overview

Fake job postings can mislead job seekers and may be used for fraudulent purposes. This project uses machine learning to identify suspicious job postings based on information such as job description, company profile, requirements, employment type, education, industry, and other job-related features.

## Features

- Job title
- Company profile
- Job description
- Employment type
- Required experience
- Required education
- Industry
- Function
- Benefits
- Company information
- Presence of email, URL, logo, and questions

## Machine Learning Workflow

1. Data loading
2. Data preprocessing
3. Missing value handling
4. Feature engineering
5. Categorical feature encoding
6. Train-test split
7. Decision Tree model training
8. Model evaluation
9. Fake/Real job prediction
10. Streamlit web interface

## Model

The project uses a **Decision Tree Classifier** for binary classification.

The target classes are:

- `REAL JOB`
- `FAKE JOB`

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Matplotlib
- Seaborn

## Project Structure

```text
Fake-Job-Posting-Detection/
│
├── app.py
├── Fake_Job_Posting_Detection.ipynb
├── fake_job_model.pkl
├── model_features.pkl
├── requirements.txt
└── README.md
