# agents/summary_agent.py
from dotenv import load_dotenv
load_dotenv()

def generate_summary(transcript):
    return "Dummy Summary:\n" + transcript[:200] + "..."
