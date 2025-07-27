# backend/app/services/qloo_service.py

from typing import Dict, List
import httpx
from app.utils.config import settings
import logging

logger = logging.getLogger("taste-tracker")

class QlooService:
    BASE = settings.QLOO_API_BASE.rstrip("/")  # e.g. https://hackathon.api.qloo.com
    HEADERS = {
        "Content-Type": "application/json",
        "X-Api-Key": settings.QLOO_API_KEY
    }
    DOMAIN_MAP = {
        "music":   "urn:entity:artist",
        "film":    "urn:entity:movie",
        "fashion": "urn:entity:brand",
        "dining":  "urn:entity:place",
        "travel":  "urn:entity:destination",
    }

    async def search_entity(self, name: str, entity_type: str = "urn:entity:brand") -> str:
        """
        Hit both /v2/search and /search and normalize whatever shape comes back.
        """
        params = {"query": name, "types": entity_type, "limit": 1}
        async with httpx.AsyncClient() as client:
            for path in ("/v2/search", "/search"):
                url = f"{self.BASE}{path}"
                r = await client.get(url, params=params, headers=self.HEADERS)
                if r.status_code == 404:
                    continue
                r.raise_for_status()
                data = r.json()

                # try both top-level and nested result shapes
                hits = data.get("entities") or data.get("results", {}).get("entities", [])
                if not hits:
                    logger.debug(f"No hits in {path} for {name}: {data!r}")
                    continue

                # success!
                entity = hits[0]
                logger.debug(f"Found entity via {path}: {entity!r}")
                return entity["entity_id"]

        raise ValueError(f"No {entity_type} found for '{name}'")

    async def get_affinities(self, brand_name: str) -> Dict[str, List[str]]:
        brand_id = await self.search_entity(brand_name, entity_type="urn:entity:brand")
        affinities: Dict[str, List[str]] = {}

        async with httpx.AsyncClient() as client:
            for domain, filter_type in self.DOMAIN_MAP.items():
                params = {
                    "filter.type": filter_type,
                    "signal.interests.entities": brand_id,
                    "limit": 5
                }
                r = await client.get(f"{self.BASE}/v2/insights", params=params, headers=self.HEADERS)
                r.raise_for_status()
                ents = r.json().get("results", {}).get("entities", [])
                affinities[domain] = [e["name"] for e in ents]

        return affinities

qloo = QlooService()
