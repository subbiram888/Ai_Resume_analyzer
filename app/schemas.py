from pydantic import BaseModel, Field
from typing import List, Optional

class SkillGapAnalysis(BaseModel):
    matching_skills: List[str] = Field(description="Skills present in both resume and job description")
    missing_skills: List[str] = Field(description="Key skills required in job description missing from resume")

class ResumeAnalysisResult(BaseModel):
    candidate_name: Optional[str] = Field(description="Extracted full name of candidate")
    candidate_email: Optional[str] = Field(description="Extracted email address")
    overall_match_score: int = Field(description="Relevance score from 0 to 100")
    summary: str = Field(description="Brief executive summary of the candidate's alignment with the job")
    strengths: List[str] = Field(description="Key profile strengths for this role")
    weaknesses: List[str] = Field(description="Areas where candidate falls short")
    skill_gap: SkillGapAnalysis
    improvements: List[str] = Field(description="Actionable recommendations to improve the resume")