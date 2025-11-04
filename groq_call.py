import os
import requests
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("API_key")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama-3.1-8b-instant"


def call_llm(prompt: str):
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": [{"role": "user", "content": prompt.strip()}],
        "temperature": 0.7,
        "max_tokens": 1500
    }

    try:
        response = requests.post(GROQ_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        content = data["choices"][0]["message"]["content"].strip()
        print("\n Raw LLM O/p:\n", content)
        return content
    except Exception as e:
        print(" Groq request failed:", e)
        return f"Error calling Groq: {e}"
