from fastapi import APIRouter, Query
from app.services import qloo_service

router = APIRouter()

@router.get("/")
def get_taste_profile(brand: str = Query(...)):
    entity = qloo_service.get_entity_id(brand)
    if not entity.get("entity_id"):
        return {"error": "Brand not found"}

    data = qloo_service.get_affinities(entity["entity_id"])
    return {"brand": brand, "affinities": data}
