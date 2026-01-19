"""
Rate limiter module for FastAPI application.

This module provides rate limiting functionality using an in-memory cache backend.
It supports both HTTP requests and WebSocket connections with configurable limits
and time windows.

Features:
    - Request rate limiting by IP address and path
    - WebSocket connection rate limiting
    - Thread-safe caching with TTL support
    - Customizable identifiers and callbacks
    - Comprehensive logging for monitoring

file: backend/backend/rate_limiter/__init__.py
"""

from math import ceil
from typing import (
    Callable,
    Optional,
    Union
)

from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import Response
from starlette.status import HTTP_429_TOO_MANY_REQUESTS
from starlette.websockets import WebSocket
from backend.cache import get_cache_manager

# Logger
from backend.logger import logger

async def default_identifier(request: Union[Request, WebSocket]):
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        ip = forwarded.split(",")[0]
    else:
        ip = request.client.host
    return ip + ":" + request.scope["path"]


async def http_default_callback(request: Request, response: Response, pexpire: int):
    """
    default callback when too many requests
    :param request:
    :param pexpire: The remaining milliseconds
    :param response:
    :return:
    """
    expire = ceil(pexpire / 1000)
    client_ip = request.client.host if request.client else "unknown"
    logger.warning(f"Rate limit exceeded for HTTP request: client={client_ip}, path={request.url.path}, method={request.method}, retry_after={expire}s")
    raise HTTPException(
        HTTP_429_TOO_MANY_REQUESTS, "Too Many Requests", headers={"Retry-After": str(expire)}
    )


async def ws_default_callback(ws: WebSocket, pexpire: int):
    """
    default callback when too many requests
    :param ws:
    :param pexpire: The remaining milliseconds
    :return:
    """
    expire = ceil(pexpire / 1000)
    client_ip = ws.client.host if ws.client else "unknown"
    logger.warning(f"Rate limit exceeded for WebSocket: client={client_ip}, retry_after={expire}s")
    raise HTTPException(
        HTTP_429_TOO_MANY_REQUESTS, "Too Many Requests", headers={"Retry-After": str(expire)}
    )


class FastAPILimiter:
    prefix: Optional[str] = None
    identifier: Optional[Callable] = None
    http_callback: Optional[Callable] = None
    ws_callback: Optional[Callable] = None

    @classmethod
    async def init(
        cls,
        prefix: str = "fastapi-limiter",
        identifier: Callable = default_identifier,
        http_callback: Callable = http_default_callback,
        ws_callback: Callable = ws_default_callback,
    ) -> None:
        cls.prefix = prefix
        cls.identifier = identifier
        cls.http_callback = http_callback
        cls.ws_callback = ws_callback
        logger.info(f"FastAPILimiter initialized: prefix={prefix}")

    @classmethod
    def get_cache(cls):
        """Get the cache manager instance."""
        return get_cache_manager()

    @classmethod
    async def close(cls) -> None:
        logger.info("FastAPILimiter closed")
        pass
