from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .agent import run_agent
from .memory import add_message, clear_session

app = FastAPI(title="Relax AI Agent", version="1.0.0")

class ChatRequest(BaseModel):
    session_id: str = Field(min_length=1, max_length=100)
    message: str = Field(min_length=1, max_length=12000)

class ChatResponse(BaseModel):
    session_id: str
    response: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        answer = run_agent(request.session_id, request.message)
        add_message(request.session_id, "user", request.message)
        add_message(request.session_id, "assistant", answer)
        return ChatResponse(session_id=request.session_id, response=answer)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

@app.delete("/chat/{session_id}")
def delete_chat(session_id: str):
    clear_session(session_id)
    return {"status": "cleared", "session_id": session_id}
