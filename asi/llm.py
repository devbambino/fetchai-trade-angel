import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve API key
api_key = os.getenv("ASI1_LLM_API_KEY")

# ASI1-Mini LLM API endpoint
url = "https://api.asi1.ai/v1/chat/completions"

# Define headers for API requests
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

def query_llm(query):
    """Query ASI1-Mini LLM with a given prompt"""
    data = {
        "messages": [{"role": "user", "content": query}],
        "conversationId": None,
        "model": "asi1-mini"
    }

    try:
        with requests.post(url, headers=headers, json=data) as response:
            output = response.json()
            return output["choices"][0]["message"]["content"]
    
    except requests.exceptions.RequestException as e:
        return str(e)