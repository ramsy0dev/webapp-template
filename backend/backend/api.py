"""
This is where our api is defined, along side the routes.


file:backend/backend/api.py
"""

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from contextlib import asynccontextmanager

# Routes
from backend.routes import routes

# Rate limiter
from backend.rate_limiter import FastAPILimiter

# Logger
from backend.logger import logger

@asynccontextmanager
async def lifespan(api: FastAPI):
    """
    Start up and Shutdown event handler
    """
    # Start up events

    # Initialize the cache manager
    from backend.cache.cache_manager import init_cache_manager
    init_cache_manager(max_size=2000, ttl=3600)
    
    await FastAPILimiter.init()
    yield

    # Shutdown events

    await FastAPILimiter.close()


# Initialize the api
api = FastAPI(
    lifespan=lifespan
)

# Adding middlewares
middlewares = []
for middleware in middlewares:
    api.add_middleware(middleware)


for router in routes:
    api.include_router(router)
