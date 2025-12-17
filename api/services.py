import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_answer(question):
    if not GROQ_API_KEY:
        return "AI service not configured"
    return f"This is an AI-generated draft answer for: {question}"
