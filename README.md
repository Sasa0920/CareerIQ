# 📄 CareerIQ – AI-Powered Job Recommendation System

CareerIQ is an AI-powered career assistant that analyzes a user’s resume and provides personalized career insights along with real-time job recommendations from LinkedIn and Indeed. The system combines Large Language Models (LLMs), external job APIs, and an agent-ready backend architecture to deliver intelligent career guidance through a simple web interface.

---

## 🚀 Features

- 📤 Upload a resume (PDF format)
- 📑 AI-generated resume summary
- 🛠️ Skill gap analysis and improvement suggestions
- 🚀 Personalized future career roadmap
- 🔎 Intelligent job keyword extraction
- 💼 Real-time job recommendations from:
  - LinkedIn
  - Indeed
- 🤖 Agent-ready backend using MCP (Model Context Protocol)

---

## 🧠 How the Project Works

1. The user uploads a resume through the Streamlit web interface.
2. Text is extracted from the PDF resume.
3. A Large Language Model (Groq) analyzes the resume to:
   - Summarize skills, education, and experience
   - Identify missing skills and certifications
   - Suggest a future career roadmap
4. The AI generates relevant job search keywords from the resume analysis.
5. Job listings are fetched from LinkedIn and Indeed using the Apify API.
6. Job-fetching functions are exposed as tools through an MCP server, allowing AI agents to call them intelligently.
7. The final insights and job recommendations are displayed to the user in a clean and interactive UI.

---


---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **LLM:** Groq (via LangChain)
- **Job Data:** Apify API
- **PDF Processing:** PyMuPDF (fitz)
- **Agent Tools:** MCP (Model Context Protocol)
- **Environment Management:** uv
- **APIs:** LinkedIn & Indeed Scrapers (Apify Actors)

---





