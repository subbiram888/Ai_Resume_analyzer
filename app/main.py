from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.utils import extract_text_from_pdf_bytes
from app.analyzer import run_resume_analysis
from app.schemas import ResumeAnalysisResult

app = FastAPI(
    title="Resume Analyzer AI API",
    description="FastAPI + LangChain service to evaluate resumes against Job Descriptions",
    version="1.0.0"
)

# Configure CORS Middleware
origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
    "*"  # Allows all origins during local development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Resume Analyzer API is up and running!"}

@app.post("/analyze", response_model=ResumeAnalysisResult)
async def analyze_resume(
    job_description: str = Form(..., description="The job description text"),
    file: UploadFile = File(..., description="Resume PDF file")
):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    pdf_bytes = await file.read()
    resume_text = extract_text_from_pdf_bytes(pdf_bytes)
    
    if not resume_text.strip():
        raise HTTPException(status_code=400, detail="Could not extract text from the provided PDF.")
    
    analysis_result = await run_resume_analysis(
        job_description=job_description,
        resume_text=resume_text
    )
    
    return analysis_result