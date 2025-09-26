# src/test_bedrock.py
import boto3
import json

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
try:
    response = bedrock.invoke_model(
        modelId="anthropic.claude-3-5-sonnet-20240620-v1:0",
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 200,
            "messages": [{"role": "user", "content": "Hello, are you working?"}]
        })
    )
    result = json.loads(response['body'].read())
    print("✅ Bedrock is working!")
    print(result['content'][0]['text'])
except Exception as e:
    print(f"❌ Error: {e}")