import streamlit as st
from src.helper import extract_text_from_pdf, ask_llm
from src.job_api import fetch_linkdin_jobs, fetch_indeed_jobs

# Page Config 
st.set_page_config(
    page_title="CareerIQ",
    page_icon="📄",
    layout="wide"
)

# Custom CSS 
st.markdown("""
<style>
body {
    background-color: #0e1117;
}

.main-title {
    font-size: 48px;
    font-weight: 800;
    background: linear-gradient(90deg, #6a5acd, #00c9a7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    font-size: 18px;
    color: #cfcfcf;
    margin-bottom: 30px;
}

.section-title {
    font-size: 26px;
    font-weight: 700;
    margin-top: 30px;
}

.card {
    background-color: #161b22;
    padding: 20px;
    border-radius: 14px;
    margin-bottom: 20px;
    border: 1px solid #262730;
    box-shadow: 0 0 15px rgba(0,0,0,0.3);
}

.job-card {
    background-color: #0f172a;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 15px;
    border-left: 5px solid #6a5acd;
}

.job-title {
    font-size: 18px;
    font-weight: 700;
    color: #ffffff;
}

.job-company {
    color: #9ca3af;
    font-size: 14px;
}

.job-link a {
    text-decoration: none;
    color: #22c55e;
    font-weight: 600;
}

hr {
    border: none;
    height: 1px;
    background-color: #262730;
    margin: 30px 0;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-title">CareerIQ</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Upload your resume and get AI-powered career insights and job recommendations from LinkedIn & Indeed.</div>',
    unsafe_allow_html=True
)

# File Upload 
uploaded_file = st.file_uploader(
    "📤 Upload your resume (PDF only)",
    type=["pdf"]
)

# Resume Analysis 
if uploaded_file:
    with st.spinner("📄 Extracting resume content..."):
        resume_text = extract_text_from_pdf(uploaded_file)

    with st.spinner("🧠 Generating resume summary..."):
        summary = ask_llm(
            f"Summarize this resume highlighting skills, education, and experience:\n\n{resume_text}"
        )

    with st.spinner("🛠️ Identifying skill gaps..."):
        skills_gap = ask_llm(
            f"Analyze this resume and highlight missing skills, certifications, and experiences:\n\n{resume_text}"
        )

    with st.spinner("🚀 Creating future roadmap..."):
        roadmap = ask_llm(
            f"Based on this resume, suggest a future career roadmap including skills, certifications, and industry exposure:\n\n{resume_text}"
        )

    st.success("✅ Resume analysis completed!")

    # Display Results
    st.markdown('<div class="section-title">📑 Resume Summary</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="card">{summary}</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">🛠️ Skill Gaps & Improvements</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="card">{skills_gap}</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">🚀 Career Roadmap</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="card">{roadmap}</div>', unsafe_allow_html=True)

    # Job Search 
    if st.button("🔎 Find Matching Jobs", use_container_width=True):
        with st.spinner("🔍 Extracting job keywords..."):
            keywords = ask_llm(
                f"Based on this resume summary, suggest the best job titles and keywords for searching jobs. "
                f"Return only a comma-separated list.\n\nSummary: {summary}"
            )
            search_keywords_clean = keywords.replace("\n", "").strip()

        st.success(f"🎯 Job Search Keywords: {search_keywords_clean}")

        primary_keyword = search_keywords_clean.split(",")[0].strip()

        with st.spinner("💼 Fetching jobs from LinkedIn & Indeed..."):
            linkedin_jobs = fetch_linkdin_jobs(primary_keyword, rows=60)
            indeed_jobs = fetch_indeed_jobs(primary_keyword, rows=60)

        # LinkedIn Jobs 
        st.markdown('<div class="section-title">💼 LinkedIn Jobs</div>', unsafe_allow_html=True)

        if linkedin_jobs:
            for job in linkedin_jobs:
                st.markdown(f"""
                <div class="job-card">
                    <div class="job-title">{job.get('title')}</div>
                    <div class="job-company">{job.get('companyName')} • {job.get('location')}</div>
                    <div class="job-link"><a href="{job.get('link')}" target="_blank">View Job →</a></div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No LinkedIn jobs found.")

        # Indeed Jobs
        st.markdown('<div class="section-title">💼 Indeed Jobs</div>', unsafe_allow_html=True)

        if indeed_jobs:
            for job in indeed_jobs:
                st.markdown(f"""
                <div class="job-card">
                    <div class="job-title">{job.get('title')}</div>
                    <div class="job-company">{job.get('companyName')} • {job.get('location')}</div>
                    <div class="job-link"><a href="{job.get('url')}" target="_blank">View Job →</a></div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No Indeed jobs found.")
