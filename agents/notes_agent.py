import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_notes(transcript):
    model = genai.GenerativeModel('gemini-pro')
    prompt = (
        "Based on the following YouTube transcript, create clear and concise notes as bullet points:\n\n"
        f"{transcript}"
    )
    response = model.generate_content(prompt)
    return response.text
