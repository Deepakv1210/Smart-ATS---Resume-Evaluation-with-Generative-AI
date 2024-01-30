# Smart ATS - Resume Evaluation with Generative AI

Welcome to Smart ATS, a Streamlit app powered by Google's GenerativeAI. This tool simulates an experienced Application Tracking System (ATS) with expertise in the tech field, including software engineering, data science, data analysis, and big data engineering. Use Smart ATS to improve your resume and receive personalized feedback based on a provided job description.

## Features

- Upload your resume in PDF format.
- Paste the job description for tailored evaluation.
- Get a detailed response with a percentage match, missing keywords, and a profile summary.

## Example Response Format

```json
{
  "JD Match": "75%",
  "Missing Keywords": ["Java", "Machine Learning"],
  "Profile Summary": "Skilled professional with expertise in software engineering..."
}
