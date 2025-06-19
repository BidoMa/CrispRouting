from database import get_unanswered_assignments, mark_as_escalated
from crisp_api import reassign_operator
from datetime import datetime, timedelta

now = datetime.utcnow()
limite = now - timedelta(minutes=15)

for assignment in get_unanswered_assignments():
    if assignment['asignado_ts'] < limite and not assignment['escalado']:
        reassign_operator(assignment['session_id'])
        mark_as_escalated(assignment['session_id'])
