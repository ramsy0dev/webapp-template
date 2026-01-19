"""
This file contains classes for handling rate limiting routes and websockets


file: backend/backend/rate_limiter/depends.py
"""

import time
import logging

from typing import (
    Annotated,
    Callable,
    Optional
)

from pydantic import Field
from starlette.requests import Request
from starlette.responses import Response
from starlette.websockets import WebSocket

from backend.rate_limiter import FastAPILimiter

# Logger
from backend.logger import logger

class RateLimiter:
    def __init__(
        self,
        times: Annotated[int, Field(ge=0)] = 1,
        milliseconds: Annotated[int, Field(ge=-1)] = 0,
        seconds: Annotated[int, Field(ge=-1)] = 0,
        minutes: Annotated[int, Field(ge=-1)] = 0,
        hours: Annotated[int, Field(ge=-1)] = 0,
        identifier: Optional[Callable] = None,
        callback: Optional[Callable] = None,
    ):
        self.times = times
        # Convert all time units to seconds for cache TTL
        self.ttl_seconds = milliseconds // 1000 + seconds + 60 * minutes + 3600 * hours
        # Ensure minimum TTL of 1 second
        self.ttl_seconds = max(1, self.ttl_seconds)
        self.identifier = identifier
        self.callback = callback

    async def _check(self, key):
        cache = FastAPILimiter.get_cache()
        try:
            # Try to get current count
            current = cache.get(key)
            
            if current is None:
                # First request, set initial count with timestamp
                cache.set(key, (1, time.time() + self.ttl_seconds))
                logger.debug(f"Rate limiter NEW KEY: key={key}, ttl={self.ttl_seconds}s, limit={self.times}")
                return 0  # No rate limit exceeded
            
            count, expiry = current
            
            # Check if entry has expired
            if time.time() > expiry:
                # Expired, reset counter
                cache.set(key, (1, time.time() + self.ttl_seconds))
                logger.debug(f"Rate limiter RESET EXPIRED: key={key}, ttl={self.ttl_seconds}s")
                return 0
            
            if count >= self.times:
                # Rate limit exceeded, return remaining TTL in milliseconds
                remaining = (expiry - time.time())
                remaining_ms = max(0, int(remaining * 1000))
                logger.info(f"Rate limiter LIMIT EXCEEDED: key={key}, count={count}, limit={self.times}, remaining={remaining:.2f}s")
                return remaining_ms
            
            # Increment count
            cache.set(key, (count + 1, expiry))
            logger.debug(f"Rate limiter INCREMENT: key={key}, count={count + 1}/{self.times}")
            return 0  # No rate limit exceeded
            
        except Exception as e:
            logger.error(f"Rate limiter error for key={key}: {str(e)}", exc_info=True)
            raise Exception(f"Cache rate limiter error: {str(e)}")

    async def __call__(self, request: Request, response: Response):
        cache = FastAPILimiter.get_cache()
        if not cache:
            logger.error("Cache not initialized for rate limiter")
            raise Exception("You must call FastAPILimiter.init in startup event of fastapi!")
        
        client_ip = request.client.host if request.client else "unknown"
        route_index = 0
        dep_index = 0
        for i, route in enumerate(request.app.routes):
            if route.path == request.scope["path"] and request.method in route.methods:
                route_index = i
                for j, dependency in enumerate(route.dependencies):
                    if self is dependency.dependency:
                        dep_index = j
                        break

        # moved here because constructor run before app startup
        identifier = self.identifier or FastAPILimiter.identifier
        callback = self.callback or FastAPILimiter.http_callback
        rate_key = await identifier(request)
        key = f"{FastAPILimiter.prefix}:{rate_key}:{route_index}:{dep_index}"
        
        logger.debug(f"HTTP rate limit check: client={client_ip}, path={request.url.path}, method={request.method}, key={key}")
        pexpire = await self._check(key)
        
        if pexpire != 0:
            logger.warning(f"HTTP rate limit triggered: client={client_ip}, path={request.url.path}, method={request.method}")
            return await callback(request, response, pexpire)
        
        logger.debug(f"HTTP rate limit passed: client={client_ip}, path={request.url.path}, method={request.method}")


class WebSocketRateLimiter(RateLimiter):
    async def __call__(self, ws: WebSocket, context_key=""):
        cache = FastAPILimiter.get_cache()
        if not cache:
            logger.error("Cache not initialized for WebSocket rate limiter")
            raise Exception("You must call FastAPILimiter.init in startup event of fastapi!")
        
        client_ip = ws.client.host if ws.client else "unknown"
        identifier = self.identifier or FastAPILimiter.identifier
        rate_key = await identifier(ws)
        key = f"{FastAPILimiter.prefix}:ws:{rate_key}:{context_key}"
        
        logger.debug(f"WebSocket rate limit check: client={client_ip}, key={key}")
        pexpire = await self._check(key)
        callback = self.callback or FastAPILimiter.ws_callback
        
        if pexpire != 0:
            logger.warning(f"WebSocket rate limit triggered: client={client_ip}")
            return await callback(ws, pexpire)
        
        logger.debug(f"WebSocket rate limit passed: client={client_ip}")
