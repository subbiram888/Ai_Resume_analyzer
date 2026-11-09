import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from app.schemas import ResumeAnalysisResult

load_dotenv()

# Initialize Gemini model
# Recommended models: "gemini-2.5-flash" or "gemini-1.5-pro"
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0.0
)

# Bind structured output schema (uses Gemini's native JSON Schema engine)
structured_llm = llm.with_structured_output(ResumeAnalysisResult)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert Technical Recruiter and ATS Optimization Engine. Analyze the candidate's resume against the job description."),
    ("user", "Job Description:\n{job_description}\n\nResume Content:\n{resume_text}")
])

chain = prompt | structured_llm

async def run_resume_analysis(job_description: str, resume_text: str) -> ResumeAnalysisResult:
    return await chain.ainvoke({
        "job_description": job_description,
        "resume_text": resume_text
    })