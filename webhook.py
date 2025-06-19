from fastapi import FastAPI, Request
from database import save_asignacion, init_db
from datetime import datetime

app = FastAPI()
init_db()

@app.post("/webhook")
async def receive_event(request: Request):
    data = await request.json()
    if data.get("event") == "conversation:assigned":
        session_id = data["data"]["session_id"]
        operator_id = data["data"]["operator_id"]
        ts = datetime.utcnow().isoformat()
        save_asignacion(session_id, operator_id, ts)
    return {"ok": True}
