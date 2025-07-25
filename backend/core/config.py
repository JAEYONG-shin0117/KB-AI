import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DB_URL = os.getenv("DB_URL", "sqlite:///./test.db")

# core/utils.py
def clean_text(text: str) -> str:
    return text.strip().replace('\n', ' ').replace('\r', '')
