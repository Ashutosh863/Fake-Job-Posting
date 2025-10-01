import os
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

model_path = Path("best_model.pkl")
model_data = joblib.load(model_path)

st.title("Job Posting Fraud Detection")
st.write("Enter a job details below to check if the posting is fraudlent or real")

# User inputs
title_length = st.number_input("Title_length",min_value=0,value=20)
company_profile_length = st.number_input("Comapny Profile Length",min_value=0,value=150)
description_length = st.number_input("Description length",min_value=0,value=200)
requirements_length = st.number_input("Requirements length",min_value=0,value=200)
benefits_length = st.number_input("Benefits length",min_value=0,value=50)

telecommuting = st.selectbox("Telecommuting",[0,1])
has_company_logo = st.selectbox("Has Comapny Logo",[0,1])
has_questions = st.selectbox("Has questions",[0,1])

employment_type = st.selectbox("Employment type",["Full-time","Part-time","Contract","Other"])
required_experience = st.selectbox("Required experience",["Internship","Entry Level","Mid-Senior Level","Director","Associate","Not Applicable"])
required_education = st.selectbox("Required Education",["High School","Bachelor's Degree","Master's Degree","phD","Other"])

industry = st.text_input("Industry","Information Technology")
function = st.text_input("Function","Engineering")
location = st.text_input("Location","New York, NY")

# Preprare Input
input_data = pd.DataFrame([{
    "title_length":title_length,
    "company_profile_length":company_profile_length,
    "description_length":description_length,
    "requiremtns_length":requirements_length,
    "benefits_length":benefits_length,
    "telecommuting":telecommuting,
    "has_company_logo":has_company_logo,
    "has_questions":has_questions,
    "employment_type":employment_type,
    "required_expeirence":required_experience,
    "required_education":required_education,
    "industry":industry,
    "function":function,
    "location":location
}])

#Predict
if st.button("Predict"):
    pred = model_data.predict(input_data)[0]
    if pred == 1:
        st.error("🚨 This job posting is predicted to be FRAUDULENT.")
    else:
        st.success("✅ This job posting looks REAL.")