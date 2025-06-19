import requests

IDENTIFIER = "4a06014f-69b9-402c-b134-e20c6d636381"
KEY = "39751ba091aa4a438790484b983acbd101e74d8831b95a35f16ccbae90f5db49"
WEBSITE_ID = "acf40c5a-229e-42dd-a9c0-071c24d948e3"

def reassign_operator(session_id):
    url = f"https://api.crisp.chat/v1/website/{WEBSITE_ID}/conversations/{session_id}/operator"
    headers = {
        "Authorization": f"Basic {IDENTIFIER}:{KEY}"
    }
    data = {
        "operator_id": "NUEVO_OPERATOR_ID"  # ← reemplazar por el ID deseado
    }
    res = requests.patch(url, json=data, headers=headers)
    print(f"Reasignado {session_id} → Estado: {res.status_code}")

