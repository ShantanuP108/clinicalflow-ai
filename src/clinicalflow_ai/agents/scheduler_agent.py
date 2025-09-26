# src/agents/scheduler_agent.py
from typing import Dict, Any
import json

class SchedulerAgent:
    """
    Mock Scheduler Agent for ClinicalFlow AI
    In production: will call Google Calendar API or AWS Lambda
    """
    
    def schedule_appointment(self, urgency: str, patient_id: str = "test-patient") -> Dict[str, Any]:
        if urgency == "HIGH":
            return {
                "status": "scheduled",
                "appointment_type": "emergency",
                "time_slot": "ASAP",
                "message": "Urgent appointment booked. Please proceed to clinic immediately.",
                "calendar_event_id": "evt_urgent_123"
            }
        elif urgency == "MEDIUM":
            return {
                "status": "scheduled",
                "appointment_type": "routine",
                "time_slot": "within_24h",
                "message": "Appointment scheduled within 24 hours.",
                "calendar_event_id": "evt_routine_456"
            }
        else:
            return {
                "status": "scheduled",
                "appointment_type": "routine",
                "time_slot": "next_available",
                "message": "Routine check-up scheduled.",
                "calendar_event_id": "evt_routine_789"
            }