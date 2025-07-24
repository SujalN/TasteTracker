from pydantic import BaseModel
from typing import Dict

class TasteProfileRequest(BaseModel):
    brand: str

class InsightRequest(BaseModel):
    brand_a: str
    brand_b: str
    taste_data: Dict
