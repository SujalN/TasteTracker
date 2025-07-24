import google.generativeai as genai
from app.config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def generate_brand_insights(brand_a: str, brand_b: str, taste_data: dict):
    prompt = f"""
    You are a Brand Strategist AI.

    Compare the cultural taste profiles of {brand_a} and {brand_b}.

    The data includes:
    {taste_data}

    Your task:
    1. Highlight cultural overlaps.
    2. Identify what differentiates the brands.
    3. Reveal whitespace (untapped cultural opportunities).
    4. Offer marketing strategy recommendations.

    Output Format:
    - Summary
    - Overlaps
    - Differentiators
    - Whitespace
    - Strategy
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating content: {e}"
