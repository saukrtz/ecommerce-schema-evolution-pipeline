import os
import requests
import json

def get_api_key():
    try:
        with open(".env", "r") as f:
            for line in f:
                if line.startswith("GROQ_API_KEY"):
                    return line.split("=")[1].strip()
    except FileNotFoundError:
        return None

def call_llama(prompt):
    api_key = get_api_key()
    if not api_key:
        return "Error: API Key not found."

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant assisting in a data engineering lab about schema evolution."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    test_prompt = "Explain why schema evolution is important in e-commerce pipelines in one sentence."
    print(call_llama(test_prompt))
