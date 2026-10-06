import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-6-luna")

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is missing. Create a .env file from .env.example.")
