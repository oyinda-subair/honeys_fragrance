import logging
import os

from pydantic import EmailStr
from pydantic_settings import BaseSettings

from src.honeys_fragrance.core import utils


class LoggingSettings(BaseSettings):
    LOGGING_LEVEL: int = logging.INFO


class DatabaseSettings(BaseSettings):
    DATABASE_URL: str = utils.get_db_for_by_env()
    FIRST_SUPERUSER: EmailStr = os.environ.get("FIRST_SUPERUSER")
    FIRST_SUPERUSER_PW: str = os.environ.get("FIRST_SUPERUSER_PW")


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    BASE_URL: str = os.environ.get("BASE_URL")
    ENVIRONMENT: str = utils.ENVIRONMENT
    DB_PASSWORD: str
    DB_NAME: str
    DB_USER: str
    DB_HOSTNAME: str
    FIRST_SUPERUSER: str
    FIRST_SUPERUSER_PW: str
    TEST_DB_URL: str
    LOCAL_DB_URL: str
    DATABASE_URL: str
    PYTHON_ENV: str

    db: DatabaseSettings = DatabaseSettings()
    logging: LoggingSettings = LoggingSettings()

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
