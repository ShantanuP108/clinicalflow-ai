from mangum import Mangum
from clinicalflow_ai.api import app

# Create Mangum handler for FastAPI → Lambda
handler = Mangum(app)

def lambda_handler(event, context):
    return handler(event, context)