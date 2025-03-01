import os
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    DB_USERNAME: str = "postgres"
    DB_PASSWORD: str = "my pig"
    DB_URL: str = "localhost"
    DB_NAME: str = "e_commerce_boiler"
    DB_PORT: str = "5432"
    DATABASE_URL: str = f"postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_URL}/{DB_NAME}"
    SECRET_KEY: str = os.urandom(32).hex()
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 10080
    
settings = Settings()
