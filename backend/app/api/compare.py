# backend/app/api/compare.py

import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from httpx import HTTPStatusError
from app.services.qloo_service import qloo
from app.services.llm_service import llm

logger = logging.getLogger("taste-tracker")
router = APIRouter()

class CompareRequest(BaseModel):
    brands: list[str]

class CompareResponse(BaseModel):
    profiles: dict[str, dict[str, list[str]]]
    insight: str

@router.post("/compare", response_model=CompareResponse)
async def compare_brands(req: CompareRequest):
    profiles: dict[str, dict[str, list[str]]] = {}

    # Fetch affinities for each brand
    for brand in req.brands:
        try:
            profiles[brand] = await qloo.get_affinities(brand)
        except ValueError as e:
            logger.error(f"Entity lookup error for '{brand}': {e}")
            raise HTTPException(status_code=404, detail=str(e))
        except HTTPStatusError as e:
            text = e.response.text
            logger.error(f"Qloo API error for '{brand}': {e.response.status_code} – {text}")
            raise HTTPException(status_code=400, detail=f"Qloo API error for '{brand}': {text}")
        except Exception:
            logger.exception(f"Unexpected error fetching affinities for '{brand}'")
            raise HTTPException(status_code=500, detail="Internal server error")

    # Generate the strategic insight
    try:
        insight = await llm.summarize_comparison(profiles)
    except Exception:
        logger.exception("LLM error")
        raise HTTPException(status_code=500, detail="LLM generation error")

    return {"profiles": profiles, "insight": insight}
