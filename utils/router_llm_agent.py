import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve the API key securely from .env or Streamlit secrets
api_key = os.getenv("OPENROUTER_API_KEY")

# Fallback example (if using with Streamlit)
try:
    import streamlit as st
    if "OPENROUTER_API_KEY" in st.secrets:
        api_key = st.secrets["OPENROUTER_API_KEY"]
except:
    pass

def get_llm_response(prompt: str) -> str:
    """
    Sends a prompt to OpenRouter using a free model and retrieves the LLM response.
    """

    if not api_key:
        raise Exception(" OpenRouter API key is missing. Please set OPENROUTER_API_KEY.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://openrouter.ai",  
        "X-Title": "solar-ai-assistant",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek-chat:free", 
        "messages": [
            {"role": "system", "content": "You are a solar installation expert who provides detailed, structured advice."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")
