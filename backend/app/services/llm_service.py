import os
from openai import OpenAI
from app.utils.config import settings

class LLMService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    async def summarize_comparison(self, profiles: dict) -> str:
        """
        Given taste profiles for multiple brands, generate a strategic summary.
        """
        system = "You are a brand strategist who writes concise insights."
        prompt = "Compare these taste profiles:\n\n"
        for name, profile in profiles.items():
            prompt += f"- {name}: {profile}\n"
        prompt += "\nWrite: Differentiating factors, overlaps, and white-space opportunities."

        resp = await self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ]
        )
        return resp.choices[0].message.content.strip()

llm = LLMService()