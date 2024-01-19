import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
import PyPDF2 as pdf


load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_respone(inpute):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(inpute)
    return response.text


def input_pdf_text(uploaded_file):
    reader =pdf.PdfReader(uploaded_file)
    text =""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text += str(page.extract_text())

        return text
    


input_prompt="""

Hey Act Like a skiled or very expirience ATS(Application tracking system)
with a deep understanding of tech field, software engineering, data science, data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description
you must consider the job market is very cmpetitive and yo should provede
best assistance for improve the resumes Assign the percentage Matching based on Jd and missing kewords
with high accuracy
resume:{text}
description:{jd}

I want the response one single string having the structure
{{"JD Mactch":"%", "MissingKeywords:[]","Profile summary":""}}


"""



st.title("Smart ATS")
st.text("Improve Ypur Resume ATS")

jd= st.text_area("Paste the job description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please upload the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_respone(input_prompt)
        st.subheader(response)
