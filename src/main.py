from fastapi import FastAPI
from loguru import logger

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
