import os
import pathlib
from os.path import join
from dotenv import load_dotenv

# Project Directories
ROOT = pathlib.Path(__file__).resolve().parent.parent.parent.parent

dotenv_path = join(ROOT, '.env')
load_dotenv(dotenv_path)

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
