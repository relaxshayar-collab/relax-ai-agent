# Relax AI Agent

A clean starter AI agent backend built with Python + FastAPI + OpenAI Responses API.

## Features
- Chat API with session memory
- Configurable OpenAI model
- Safe calculator tool
- Health endpoint
- Environment-variable configuration
- No API keys committed to Git

## Setup

1. Install Python 3.11+.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Copy `.env.example` to `.env`.
4. Put your OpenAI API key in `OPENAI_API_KEY`.
5. Set `OPENAI_MODEL` to a model available to your API account. The starter defaults to `gpt-6-luna`.
6. Start:
   `uvicorn app.main:app --reload`
7. Open `/docs` to test the API.

## Endpoints

- `GET /health`
- `POST /chat`

Example JSON:
```json
{
  "session_id": "demo",
  "message": "Calculate 25 * 8"
}
```

## Notes

The project uses the Responses API, which is the current API path for new OpenAI integrations. Keep secrets in `.env` and never upload them to GitHub.
