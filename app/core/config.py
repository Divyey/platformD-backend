from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str # = "changeme"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    API_PREFIX: str = "/api/v1"
    ALGORITHM: str = "HS256"
    GOOGLE_CLIENT_ID: str | None = None
    GOOGLE_CLIENT_SECRET: str | None = None
    OPENAI_API_KEY: str | None = None
    # OPENAI_KEY_1: str | None = None
    # OPENAI_KEY_2: str | None = None
    # OPENAI_KEY_3: str | None = None
    # OPENAI_KEY_4: str | None = None
    # OPENAI_KEY_5: str | None = None
    # SMTP_SERVER: str | None = None
    # SMTP_USER: str | None = None
    # SMTP_PASSWORD: str | None = None
    # REDIS_URL: str | None = None
    # VECTOR_DB_URL: str | None = None

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra="allow"  # <-- CRITICAL: prevents errors when .env has extra keys
    )

settings = Settings()
