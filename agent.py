from openai import OpenAI

from .config import OPENAI_API_KEY, OPENAI_MODEL
from .memory import get_history

client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """You are Relax AI, a helpful general-purpose personal AI assistant.
Be accurate, concise, friendly, and transparent.
Use conversation history when it is provided.
Never claim to have performed an action that you did not perform.
Never reveal API keys, tokens, or other secrets.
Only use tools that are explicitly available and safe.
If a request is unclear, ask for the missing detail.
"""

def run_agent(session_id: str, user_message: str) -> str:
    history = get_history(session_id)

    input_items = [
        {"role": "developer", "content": SYSTEM_PROMPT},
        *history,
        {"role": "user", "content": user_message},
    ]

    response = client.responses.create(
        model=OPENAI_MODEL,
        input=input_items,
    )
    return response.output_text.strip()
