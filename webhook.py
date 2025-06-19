from fastapi import FastAPI, Request
from database import save_asignacion

app = FastAPI()

@app.post("/webhook")
async def receive_webhook(request: Request):
    data = await request.json()
    
    if data.get("event") == "conversation:assigned":
        session_id = data["data"]["session_id"]
        operator_id = data["data"]["operator_id"]
        timestamp = data["timestamp"]
        save_asignacion(session_id, operator_id, timestamp)
    
    return {"ok": True}
