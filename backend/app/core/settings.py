from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import List


class Settings(BaseSettings):
    # === App ===
    APP_NAME: str = "Facturacion Electronica DIAN"
    ENVIRONMENT: str = Field(default="development")  # development | staging | production
    DEBUG: bool = Field(default=False)

    # === Security ===
    SECRET_KEY: str = Field(..., min_length=32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # === API ===
    API_V1_PREFIX: str = "/api/v1"
    ALLOWED_ORIGINS: List[str] = Field(default_factory=list)

    # === Database ===
    DATABASE_URL: str = Field(...)
    VITE_API_URL: str = Field(default="http://127.0.0.1:8000")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",  # ❗ no permite variables desconocidas
    )


settings = Settings()
