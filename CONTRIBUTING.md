# Contributing to ClinicalFlow AI

## Setup
1. `git clone https://github.com/ShantanuP108/clinicalflow-ai`
2. `cd clinicalflow-ai`
3. `pip install -e .`
4. Configure AWS credentials

## Local Development
- Test with `USE_BEDROCK=false`
- Run tests: `python -m pytest tests/`
- Format code: `black .`

## Deployment
- `sam build && sam deploy --guided`
- Update API URL in README after deployment
