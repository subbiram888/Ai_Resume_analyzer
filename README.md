# 📄 AI Resume Analyzer API

An asynchronous, production-grade backend service built with **FastAPI**, **LangChain**, and **Pydantic** that parses candidate PDF resumes, evaluates them against provided Job Descriptions (JD), and outputs structured ATS alignment feedback using Gemini AI models.

---

## 🛠️ Tech Stack & Dependencies

- **Language:** Python 3.14+
- **Web Framework:** FastAPI (Asynchronous REST API)
- **ASGI Server:** Uvicorn
- **AI Orchestration:** LangChain (`langchain-google-genai`)
- **LLM Engine:** Gemini API (`gemini-2.5-flash`)
- **Data Validation & Schemas:** Pydantic v2
- **PDF Extraction:** `pypdf` (In-memory byte-stream parsing)
- **Environment Management:** `python-dotenv`

---

## ✨ Features

- **In-Memory PDF Extraction:** Processes multipart PDF file uploads in-memory using byte streams, avoiding disk I/O bottlenecks.
- **Strict Structured JSON Returns:** Leverages LangChain's `with_structured_output` backed by Pydantic models to guarantee deterministic, schema-validated responses.
- **ATS Alignment Metrics:** Computes overall match scores, identifies key strengths and weaknesses, extracts matched/missing skills, and suggests actionable resume enhancements.
- **CORS Configured:** Pre-configured with Cross-Origin Resource Sharing middleware for seamless web client integration.
- **Self-Documenting:** Interactive API exploration via Swagger UI (`/docs`) and ReDoc (`/redoc`).

---

## 📁 Project Structure

```text
Ai_Resume_analyzer/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application, CORS settings, & endpoints
│   ├── analyzer.py      # LangChain chain & Gemini LLM orchestration
│   ├── schemas.py       # Pydantic schemas for structured LLM response
│   └── utils.py         # In-memory PDF text extraction helper
├── .env.example         # Template for environment variables
├── .gitignore           # Git exclusions (venv, .env, __pycache__)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
