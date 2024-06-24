from pydantic.v1 import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "My FastAPI Application"
    DEBUG: bool = True

    DATABASE_URL: str = 'sqlite:///./test.db'

    SECRET_KEY: str = 'hfu2fu28'
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"


settings = Settings()