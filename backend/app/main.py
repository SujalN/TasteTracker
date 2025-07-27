# backend/app/main.py

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.compare import router as compare_router
from app.utils.config import settings

# ——— Basic Logging Setup —————————————————————————————————————
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("taste-tracker")

# ——— FastAPI App Instantiation ——————————————————————————————————
app = FastAPI(title="TasteTracker API")

# ——— CORS Configuration ——————————————————————————————————————
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],                      # GET, POST, OPTIONS, …
    allow_headers=["*"],                      # all headers
)

# ——— Include Compare Router ————————————————————————————————————
app.include_router(compare_router, prefix="/api")

# ——— Root Health‑Check Endpoint ——————————————————————————————
@app.get("/")
async def root():
    return {"message": "TasteTracker is alive!"}
