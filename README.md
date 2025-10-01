Fake Job Posting Detection

Table of Contents
Project Overview
Dataset
Features
Machine Learning Models
Installation
Usage
Results
Deployment
Future Improvements



Project Overview:
This project aims to detect fake job postings using machine learning techniques without relying on NLP-heavy approaches. The goal is to predict whether a job posting is real or fake based on its features, helping job seekers and platforms filter fraudulent listings.

Dataset
The dataset contains job postings with various attributes, such as company profile, job description, requirements, and more. It is publicly available and widely used for fake job detection tasks.

Key points about the dataset:

Number of samples: ~17,000+ job postings
Target variable: fraudulent (0 = real, 1 = fake)

Features include:
title_length
company_profile_length
description_length
requirements_length
benefits_length
telecommuting
has_company_logo
has_questions
employment_type
required_experience
required_education
industry
function
location

Features
Text-based lengths: title_length, description_length, requirements_length
Binary features: telecommuting, has_company_logo, has_questions
Categorical features: employment_type, required_experience, required_education, industry, function, location
These features were processed using SimpleImputer, OneHotEncoder, and StandardScaler in a pipeline to prepare the data for machine learning models.
Machine Learning Models

Several models were trained and evaluated to detect fake job postings:
Logistic Regression
Decision Tree Classifier
Random Forest Classifier
Gradient Boosting Classifier
XGBoost
Support Vector Machine
LightGBM (Best performing)
The project uses scikit-learn pipelines to ensure clean preprocessing and model evaluation.

Installation
Clone the repository and install the required packages:
git clone <repo-link>
cd fake-job-posting
pip install -r requirements.txt

Usage
Training & Evaluation:
Run the main notebook or script to preprocess data, train models, and evaluate results.

Streamlit Deployment:
Launch the Streamlit app for interactive predictions:
streamlit run app.py


Input:
Users can input job posting details, and the model predicts if the posting is real or fake.

Results:
Best model: LightGBM
Evaluation metrics:
Accuracy: 0.89
Precision: 0.88
Recall: 0.44
F1-Score: 0.59
The model performs well in detecting real postings and moderately in detecting fake postings.

Deployment:
The project includes a Streamlit app for real-time predictions. Users can enter job posting details and instantly get predictions.

Features of the app:

Clean input forms
Instant predictions
Easy to use
Future Improvements
Integrate NLP-based features for better text understanding.
Balance the dataset for improved recall on fake postings.
Deploy as a web app using Heroku or AWS.
Include feature importance visualization for model explainability.