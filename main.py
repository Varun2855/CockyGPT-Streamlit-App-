import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
base_url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "HTTP-Referer": "http://localhost",  # Replace with your domain if deployed
    "X-Title": "CockyGPT Streamlit"
}

def get_cocky_reply(user_input):
    payload = {
        "model": "mistralai/mistral-7b-instruct",  # or "openai/gpt-3.5-turbo" if using OpenRouter's version
        "messages": [
            {"role": "system", "content": "You are a bratty and cocky bot who gives short and snarky comments but also gets the answer right."},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7,
        "max_tokens": 100
    }

    response = requests.post(base_url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

# Streamlit UI
st.set_page_config(page_title="CockyGPT")
st.title("🤖 CockyGPT")

user_input = st.text_input("What's up?")

if st.button("Enter") and user_input:
    with st.spinner("Being a smartass..."):
        reply = get_cocky_reply(user_input)
        st.success(reply)
