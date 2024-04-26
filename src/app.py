from asgi_correlation_id import CorrelationIdMiddleware
from fastapi import FastAPI

from src.middleware.requests import HttpRequestLoggingMiddleware


def create_app():
    app = FastAPI()
    load_middlewares(app)
    return app


def load_middlewares(app: FastAPI):
    app.add_middleware(HttpRequestLoggingMiddleware)
    app.add_middleware(CorrelationIdMiddleware)
