# ClinicalFlow AI
An autonomous healthcare operations agent for the AWS AI Agent Global Hackathon.

## Features
- Real-time clinical triage using **Claude 3.5 Sonnet on Amazon Bedrock**
- Appointment scheduling based on urgency
- End-to-end agentic workflow

## Setup
1. `pip install -e .`
2. Set AWS credentials (`~/.aws/credentials`)
3. Run: `python src/clinicalflow_ai/orchestrator.py`

## Architecture
![Architecture Diagram](docs/architecture.png)
