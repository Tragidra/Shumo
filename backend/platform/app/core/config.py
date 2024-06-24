from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Основные настройки приложения
    APP_NAME: str = "CBM_API"
    DEBUG: bool = True

    # Настройки базы данных
    DATABASE_URL: str = 'sqlite:///./test.db'

    # Настройки безопасности
    SECRET_KEY: str = 'hfu2fu28'
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"


settings = Settings()
