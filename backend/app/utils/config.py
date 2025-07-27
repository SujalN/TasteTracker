import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    QLOO_API_KEY: str = os.getenv("QLOO_API_KEY", "")
    QLOO_API_BASE: str = os.getenv("QLOO_API_BASE", "https://api.qloo.com")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    # Or for Claude:
    # ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")

settings = Settings()