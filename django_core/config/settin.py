from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    DATABASE_URL: str
    TELEGRAM_TOKEN: str
    GROQ_API_KEY: str
    NGROK_AUTHTOKEN: str

    class Config:
        env_file = BASE_DIR / ".env"

settings = Settings()
