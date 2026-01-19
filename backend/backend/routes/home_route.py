
from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse

# Rate limiter
from backend.rate_limiter import FastAPILimiter
from backend.rate_limiter.depends import RateLimiter

home_router = APIRouter(prefix="/api/v1", tags=["home"])

@home_router.get("/", dependencies=[Depends(RateLimiter(times=10, seconds=5))] ,response_class=ORJSONResponse, status_code=200)
async def home():
    return ORJSONResponse({"status_code": 200})
