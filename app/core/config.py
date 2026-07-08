from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # extra="ignore": docker compose 전용 변수(POSTGRES_HOST_PORT 등)가 .env에 있어도 무시
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    PROJECT_NAME: str = "UniBot Backend"

    # Database / Cache
    DATABASE_URL: str = "postgresql+asyncpg://unibot:unibot@localhost:5432/unibot"
    REDIS_URL: str = "redis://localhost:6379/0"

    # JWT
    JWT_SECRET_KEY: str = "change-me"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 14

    # Microsoft Entra ID
    MS_CLIENT_ID: str = ""
    MS_CLIENT_SECRET: str = ""
    MS_TENANT_ID: str = ""
    MS_REDIRECT_URI: str = "http://localhost:8000/auth/microsoft/callback"

    # Frontend / Cookie
    FRONTEND_URL: str = "http://localhost:3000"
    COOKIE_SECURE: bool = False

    # Seed admin
    ADMIN_EMAIL: str = "admin@example.com"
    ADMIN_PASSWORD: str = "admin1234"
    ADMIN_NAME: str = "Admin"


settings = Settings()
