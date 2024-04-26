from src.config.log import configure_logging, logger

from .app import create_app

configure_logging()

app = create_app()


@app.get("/")
async def root():
    logger.info("Hello World")
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
