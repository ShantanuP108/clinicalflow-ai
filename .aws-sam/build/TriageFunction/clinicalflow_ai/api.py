from fastapi import FastAPI
from clinicalflow_ai.orchestrator import ClinicalFlowOrchestrator
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="ClinicalFlow AI",
    description="Autonomous healthcare operations agent for AWS AI Agent Global Hackathon"
)

@app.post("/triage")
async def triage_patient(symptoms: str, patient_id: str = "test-patient"):
    orchestrator = ClinicalFlowOrchestrator()
    result = orchestrator.process_patient_request(symptoms, patient_id)
    return result