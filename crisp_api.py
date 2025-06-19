import requests

CRISP_TOKEN = "tu_token"
WEBSITE_ID = "tu_website_id"

def reassign_operator(session_id):
    url = f"https://api.crisp.chat/v1/website/{WEBSITE_ID}/conversations/{session_id}/operator"
    headers = {"Authorization": f"Bearer {CRISP_TOKEN}"}
    data = { "operator_id": "nuevo_operador" }
    
    requests.patch(url, json=data, headers=headers)
