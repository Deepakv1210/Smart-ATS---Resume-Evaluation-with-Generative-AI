import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Streamlit app title
st.title("Smart ATS")
st.text("Improve Your Resume ATS")

# Sidebar for API key input
st.sidebar.header("API Key Setup")
user_api_key = st.sidebar.text_input("Enter your Google API Key", type="password")

if user_api_key:
    os.environ['GOOGLE_API_KEY'] = user_api_key
    genai.configure(api_key=user_api_key)

# Function to get response from Gemini model
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

# Function to extract text from uploaded PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page_content = reader.pages[page]
        text += str(page_content.extract_text())
    return text

# Prompt template
input_prompt = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field, software engineering, data science, data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving the resumes. 

Assign the percentage Matching based on Jd and the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

# User inputs
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")

# Submit button
submit = st.button("Submit")

if submit:
    if not user_api_key:
        st.error("Please enter your Google API key in the sidebar to proceed.")
    elif uploaded_file is not None:
        resume_text = input_pdf_text(uploaded_file)
        prompt = input_prompt.format(text=resume_text, jd=jd)

        try:
            response = get_gemini_response(prompt)
            st.subheader("Response")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please upload a resume to proceed.")