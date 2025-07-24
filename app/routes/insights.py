from fastapi import APIRouter, Body
from app.services import llm_service

router = APIRouter()

@router.post("/")
def get_comparison_insight(payload: dict = Body(...)):
    brand_a = payload.get("brand_a")
    brand_b = payload.get("brand_b")
    taste_data = payload.get("taste_data")

    result = llm_service.generate_brand_insights(brand_a, brand_b, taste_data)
    return {"insight": result}