from typing import Dict, Any
from clinicalflow_ai.agents.triage_agent import TriageAgent
from clinicalflow_ai.agents.scheduler_agent import SchedulerAgent
import json

class ClinicalFlowOrchestrator:
    def __init__(self):
        self.triage_agent = TriageAgent()
        self.scheduler_agent = SchedulerAgent()
    
    def process_patient_request(self, symptoms: str, patient_id: str = "test-patient") -> Dict[str, Any]:
        triage_result = self.triage_agent.analyze_symptoms(symptoms)
        schedule_result = self.scheduler_agent.schedule_appointment(
            urgency=triage_result["urgency"],
            patient_id=patient_id
        )
        return {
            "triage": triage_result,
            "scheduling": schedule_result,
            "workflow_status": "completed"
        }

if __name__ == "__main__":
    orchestrator = ClinicalFlowOrchestrator()
    result = orchestrator.process_patient_request("Chest pain and shortness of breath")
    print(json.dumps(result, indent=2))