import os
import pathlib
from os.path import join
from dotenv import load_dotenv
from enum import Enum
import bcrypt

# Project Directories
ROOT = pathlib.Path(__file__).resolve().parent.parent.parent.parent

dotenv_path = join(ROOT, '.env')
load_dotenv(dotenv_path)

# Runtime environment
RUNTIME_ENV = {
    "dev": "Development",
    "test": "Test",
    "prod": "Production"
}

ENVIRONMENT = os.environ.get("PYTHON_ENV")


def get_db_for_by_env():
    if RUNTIME_ENV[ENVIRONMENT] == "Test":
        return os.environ.get("TEST_DB_URL")
    else:
        return os.environ.get("DATABASE_URL")

# User type enum


class UserRole(str, Enum):
    USER = 'user'
    ADMIN = 'admin'


# Password validation
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), bytes(hashed_password, 'utf-8'))


def get_password_hash(password: str) -> str:
    hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    return hashed_password.decode('utf8')
