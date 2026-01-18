"""
This is where our api is defined.


file:backend/backend/api.py
"""

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from contextlib import asynccontextmanager

# Logger
from backend.logger import logger

@asynccontextmanager
async def lifespan(api: FastAPI):
    """
    Start up and Shutdown event handler
    """
    yield


# Initialize the api
api = FastAPI(
    lifespan=lifespan
)

# Adding middlewares
middlewares = []
for middleware in middlewares:
    api.add_middleware(middleware)

@api.get("/", response_class=ORJSONResponse, status_code=200)
async def home():
    return ORJSONResponse([{"status_code": 200}])

