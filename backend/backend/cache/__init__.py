"""
Cache module for handling in-memory caching operations.

file: backend/backend/cache/__init__.py
"""

from backend.cache.cache_manager import (
    CacheManager,
    get_cache_manager,
    init_cache_manager,
    close_cache_manager,
)

__all__ = [
    "CacheManager",
    "get_cache_manager",
    "init_cache_manager",
    "close_cache_manager",
]
