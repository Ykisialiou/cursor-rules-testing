"""
Configuration management for pytonator application
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""

    app_name: str = "pytonator"
    version: str = "0.1.0"
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000

    # Database settings
    database_url: str = "sqlite:///./pytonator.db"

    # Security settings
    secret_key: str = "your-secret-key-here"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"


# Global settings instance
_settings = None


def get_settings() -> Settings:
    """Get application settings"""
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings
