import streamlit as st
from pypdf import PdfReader

from ats import extract_skills
from ats import calculate_ats

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("🤖 AI Resume Analyzer")

menu = st.sidebar.radio(
    "Navigation",
    [
        "📄 Upload Resume",
        "📜 Recent Analyses",
        "📊 ATS Statistics",
        "ℹ️ About Project"
    ]
)

# -----------------------------
# Upload Resume Page
# -----------------------------
if menu == "📄 Upload Resume":

    st.markdown("""
    # 🤖 AI Resume Analyzer

    ### Smart ATS Score Predictor & Career Assistant
    """)

    uploaded_file = st.file_uploader(
        "Upload Resume PDF",
        type="pdf"
    )

    job_description = st.text_area(
        "Paste Job Description Here"
    )

    if uploaded_file:

        pdf = PdfReader(uploaded_file)

        resume_text = ""

        for page in pdf.pages:
            text = page.extract_text()

            if text:
                resume_text += text

        resume_skills = extract_skills(resume_text)

        st.subheader("✅ Skills Found")

        if resume_skills:
            for skill in resume_skills:
                st.success(skill)
        else:
            st.warning("No skills detected.")

        if job_description:

            job_skills = extract_skills(job_description)

            ats_score = calculate_ats(
                resume_skills,
                job_skills
            )

            st.subheader("📊 ATS Score")

            st.metric(
                label="ATS Score",
                value=f"{ats_score}%"
            )

            st.progress(int(ats_score))

            missing_skills = list(
                set(job_skills) -
                set(resume_skills)
            )

            st.subheader("❌ Missing Skills")

            if missing_skills:
                for skill in missing_skills:
                    st.warning(skill)
            else:
                st.success(
                    "Excellent! No missing skills found."
                )

# -----------------------------
# Recent Analyses Page
# -----------------------------
elif menu == "📜 Recent Analyses":

    st.title("📜 Recent Analyses")

    st.info(
        "This feature will store previous resume analyses."
    )

    st.write("""
    Future Features:
    - View previous ATS scores
    - Compare resumes
    - Track improvements
    """)

# -----------------------------
# ATS Statistics Page
# -----------------------------
elif menu == "📊 ATS Statistics":

    st.title("📊 ATS Statistics")

    st.info(
        "Analytics dashboard coming soon."
    )

    st.write("""
    Planned Features:
    - Average ATS Score
    - Skill Match Percentage
    - Resume Performance Trends
    """)

# -----------------------------
# About Project Page
# -----------------------------
elif menu == "ℹ️ About Project":

    st.title("ℹ️ About Project")

    st.write("""
    AI Resume Analyzer is an NLP-based project that helps job seekers improve their resumes.

    Features:
    ✅ Resume PDF Parsing
    ✅ Skill Extraction
    ✅ ATS Score Calculation
    ✅ Missing Skill Detection
    ✅ Job Description Matching

    Technologies Used:
    - Python
    - Streamlit
    - NLP
    - PyPDF2
    """)

    st.success(
        "Created as an AI/ML/NLP project."
    )