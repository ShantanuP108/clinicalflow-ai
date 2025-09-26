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

**Architecture**
📊 [View Interactive Architecture Diagram](https://shantanup108.github.io/clinicalflow-ai/docs/healthcare_architecture_diagram.html)

![Architecture Preview](docs/architecture_preview.png)
