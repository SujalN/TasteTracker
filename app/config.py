import os
from dotenv import load_dotenv

load_dotenv()

QLOO_API_KEY = os.getenv("QLOO_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")