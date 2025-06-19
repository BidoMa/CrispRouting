import sqlite3
from datetime import datetime

DB = "db.sqlite"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS asignaciones (
        session_id TEXT PRIMARY KEY,
        operator_id TEXT,
        asignado_ts TEXT,
        respondido INTEGER DEFAULT 0,
        escalado INTEGER DEFAULT 0
    )''')
    conn.commit()
    conn.close()

def save_asignacion(session_id, operator_id, asignado_ts):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO asignaciones (session_id, operator_id, asignado_ts) VALUES (?, ?, ?)",
              (session_id, operator_id, asignado_ts))
    conn.commit()
    conn.close()

def get_unanswered_assignments():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''SELECT session_id, asignado_ts FROM asignaciones 
                 WHERE respondido=0 AND escalado=0''')
    rows = c.fetchall()
    conn.close()
    return [{'session_id': row[0], 'asignado_ts': row[1]} for row in rows]

def mark_as_escalated(session_id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("UPDATE asignaciones SET escalado=1 WHERE session_id=?", (session_id,))
    conn.commit()
    conn.close()
