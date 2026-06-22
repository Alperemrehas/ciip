from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Capability Interoperability Intelligence Platform"
    app_env: str = "local"
    api_v1_prefix: str = "/api/v1"

    postgres_host: str = "db"
    postgres_port: int = 5432
    postgres_db: str = "ciip"
    postgres_user: str = "ciip_user"
    postgres_password: str = "ciip_password"

    database_url: str = (
        "postgresql+psycopg://ciip_user:ciip_password@db:5432/ciip"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()