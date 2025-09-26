# tests/test_triage_agent.py
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from agents.triage_agent import TriageAgent

def test_chest_pain_triggers_high_urgency():
    agent = TriageAgent()
    result = agent.analyze_symptoms("Chest pain and trouble breathing")
    assert result["urgency"] == "HIGH"
    assert "emergency" in result["recommendation"].lower()

def test_fever_rash_triggers_medium_urgency():
    agent = TriageAgent()
    result = agent.analyze_symptoms("Fever and red rash on arms")
    assert result["urgency"] == "MEDIUM"

def test_common_cold_is_low_urgency():
    agent = TriageAgent()
    result = agent.analyze_symptoms("Runny nose and mild cough")
    assert result["urgency"] == "LOW"