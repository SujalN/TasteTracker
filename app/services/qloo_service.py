import requests
from app.config import QLOO_API_KEY

headers = {"Authorization": f"Bearer {QLOO_API_KEY}"}

def get_entity_id(brand_name: str):
    url = "https://api.qloo.com/entity_lookup"
    payload = {"entity_name": brand_name}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def get_affinities(entity_id: str, domains=None):
    url = "https://api.qloo.com/affinity"
    payload = {
        "entity_id": entity_id,
        "categories": domains or ["music", "film", "fashion", "travel"]
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()