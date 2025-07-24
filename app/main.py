from fastapi import FastAPI
from app.routes import taste_profile, insights

app = FastAPI(title="Brand Taste Analyzer", version="0.1")

# Include routes
app.include_router(taste_profile.router, prefix="/api/taste")
app.include_router(insights.router, prefix="/api/insights")

@app.get("/")
def home():
    return {"status": "Brand Taste Analyzer API Running 🚀"}