from database import get_unanswered_assignments, mark_as_escalated
from crisp_api import reassign_operator
from datetime import datetime, timedelta

limite = datetime.utcnow() - timedelta(minutes=15)

for assignment in get_unanswered_assignments():
    asignado_ts = datetime.fromisoformat(assignment["asignado_ts"])
    if asignado_ts < limite:
        reassign_operator(assignment["session_id"])
        mark_as_escalated(assignment["session_id"])
