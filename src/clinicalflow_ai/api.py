from fastapi import FastAPI
from pydantic import BaseModel
from clinicalflow_ai.orchestrator import ClinicalFlowOrchestrator
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="ClinicalFlow AI",
    description="Autonomous healthcare operations agent for AWS AI Agent Global Hackathon"
)

class TriageRequest(BaseModel):
    symptoms: str
    patient_id: str = "test-patient"

@app.post("/triage")
async def triage_patient(request: TriageRequest):
    orchestrator = ClinicalFlowOrchestrator()
    result = orchestrator.process_patient_request(
        symptoms=request.symptoms,
        patient_id=request.patient_id
    )
    return result