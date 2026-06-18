from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_TITLE: str = "NotesAPI"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "A personal notes service built with FastAPI"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
