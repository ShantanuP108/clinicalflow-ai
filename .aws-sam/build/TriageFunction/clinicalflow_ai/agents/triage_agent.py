import boto3
import json
from typing import Dict, Any
import os

class TriageAgent:
    def __init__(self):
        self.use_bedrock = os.getenv("USE_BEDROCK", "false").lower() == "true"
        if self.use_bedrock:
            self.bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
            self.model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"

    def analyze_symptoms(self, symptoms: str, patient_history: Dict[str, Any] = None) -> Dict[str, Any]:
        if self.use_bedrock:
            return self._call_bedrock(symptoms, patient_history)
        else:
            return self._mock_response(symptoms)

    def _call_bedrock(self, symptoms: str, patient_history: Dict[str, Any] = None) -> Dict[str, Any]:
        print("🧠 Calling Bedrock (Claude 3.5 Sonnet)...")
        prompt = f"""
        You are an AI clinical triage assistant. Analyze these symptoms and return a JSON response with:
        - urgency: "HIGH", "MEDIUM", or "LOW"
        - recommendation: brief advice (max 100 chars)
        - reasoning: medical justification (max 150 chars)
        - next_steps: list of actions (e.g., ["alert_physician", "schedule_urgent"])

        Symptoms: {symptoms}
        Patient history: {patient_history or 'None'}
        """
        
        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 500,
            "messages": [{"role": "user", "content": prompt}]
        })
        
        try:
            response = self.bedrock.invoke_model(
                modelId=self.model_id,
                body=body
            )
            result = json.loads(response['body'].read())
            return json.loads(result['content'][0]['text'])
        except Exception as e:
            print(f"Bedrock error: {e}. Falling back to mock.")
            return self._mock_response(symptoms)

    def _mock_response(self, symptoms: str) -> Dict[str, Any]:
        symptoms_lower = symptoms.lower()
        if "chest pain" in symptoms_lower or "breath" in symptoms_lower:
            return {
                "urgency": "HIGH",
                "recommendation": "Seek emergency care immediately.",
                "reasoning": "Chest pain + shortness of breath may indicate cardiac event.",
                "next_steps": ["alert_physician", "schedule_urgent"]
            }
        elif "fever" in symptoms_lower and "rash" in symptoms_lower:
            return {
                "urgency": "MEDIUM",
                "recommendation": "Schedule appointment within 24 hours.",
                "reasoning": "Fever with rash could indicate infection.",
                "next_steps": ["schedule_routine"]
            }
        else:
            return {
                "urgency": "LOW",
                "recommendation": "Monitor symptoms; schedule routine check-up.",
                "reasoning": "Symptoms appear non-urgent.",
                "next_steps": ["schedule_routine"]
            }