import os 
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")
    FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ENV = os.getenv("ENV", "development")

settings = Settings()