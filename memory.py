from collections import defaultdict

_sessions = defaultdict(list)

def get_history(session_id: str) -> list[dict]:
    return list(_sessions[session_id])

def add_message(session_id: str, role: str, content: str) -> None:
    _sessions[session_id].append({"role": role, "content": content})

def clear_session(session_id: str) -> None:
    _sessions.pop(session_id, None)
