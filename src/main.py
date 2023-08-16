import os
import pathlib

from fastapi import FastAPI
from loguru import logger

from dotenv import load_dotenv
from os.path import join

from src.honeys_fragrance.core.settings import settings
from src.honeys_fragrance.core.init_logger import setup_app_logging

# Project Directories
ROOT = pathlib.Path(__file__).resolve().parent.parent

dotenv_path = join(ROOT, '.env')
load_dotenv(dotenv_path)

setup_app_logging(config=settings)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    host = "0.0.0.0"
    port = 5000
    logger.info(f"Starting server on http://{host}:{port}")
    uvicorn.run(app, host=host, port=port, log_level="debug")
