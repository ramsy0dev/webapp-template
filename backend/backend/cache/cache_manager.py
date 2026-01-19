"""
External cache manager for handling in-memory caching operations.

file: backend/backend/cache/cache_manager.py
"""

import threading
import logging

from typing import (
    Any,
    Optional,
    Type,
    Dict
)
from cachetools import (
    TTLCache,
    LRUCache,
    Cache
)

# Setup logger
logger = logging.getLogger(__name__)


class CacheManager:
    """
    Centralized cache manager for handling different cache types.
    Thread-safe wrapper around cachetools caches.
    """
    
    def __init__(
        self,
        cache_type: Type[Cache] = TTLCache,
        max_size: int = 1000,
        ttl: int = 3600,
        **kwargs
    ):
        """
        Initialize the cache manager.
        
        Args:
            cache_type: Type of cache to use (TTLCache, LRUCache, etc.)
            max_size: Maximum number of items in cache
            ttl: Time-to-live in seconds (for TTLCache)
            **kwargs: Additional arguments for cache initialization
        """
        self.cache_type = cache_type
        self.max_size = max_size
        self.ttl = ttl
        self.lock = threading.RLock()
        self.cache: Optional[Cache] = None
        self._init_cache(**kwargs)
        logger.info(f"CacheManager initialized: type={cache_type.__name__}, max_size={max_size}, ttl={ttl}s")
    
    def _init_cache(self, **kwargs):
        """Initialize the cache with appropriate parameters."""
        try:
            if self.cache_type == TTLCache:
                self.cache = TTLCache(maxsize=self.max_size, ttl=self.ttl)
                logger.debug(f"TTLCache created with maxsize={self.max_size}, ttl={self.ttl}s")
            elif self.cache_type == LRUCache:
                self.cache = LRUCache(maxsize=self.max_size)
                logger.debug(f"LRUCache created with maxsize={self.max_size}")
            else:
                # For custom cache types
                self.cache = self.cache_type(maxsize=self.max_size, **kwargs)
                logger.debug(f"{self.cache_type.__name__} created with maxsize={self.max_size}")
        except Exception as e:
            logger.error(f"Failed to initialize cache: {str(e)}", exc_info=True)
            raise Exception(f"Failed to initialize cache: {str(e)}")
    
    def get(self, key: str) -> Optional[Any]:
        """
        Retrieve a value from the cache.
        
        Args:
            key: Cache key
            
        Returns:
            Cached value or None if not found
        """
        with self.lock:
            value = self.cache.get(key)
            if value is not None:
                logger.debug(f"Cache HIT: key={key}")
            else:
                logger.debug(f"Cache MISS: key={key}")
            return value
    
    def set(self, key: str, value: Any) -> None:
        """
        Store a value in the cache.
        
        Args:
            key: Cache key
            value: Value to store
        """
        with self.lock:
            self.cache[key] = value
            logger.debug(f"Cache SET: key={key}, value_type={type(value).__name__}, cache_size={len(self.cache)}/{self.max_size}")
    
    def delete(self, key: str) -> bool:
        """
        Delete a value from the cache.
        
        Args:
            key: Cache key
            
        Returns:
            True if key existed, False otherwise
        """
        with self.lock:
            if key in self.cache:
                del self.cache[key]
                logger.debug(f"Cache DELETE: key={key}, cache_size={len(self.cache)}/{self.max_size}")
                return True
            logger.debug(f"Cache DELETE FAILED: key={key} not found")
            return False
    
    def clear(self) -> None:
        """Clear all entries from the cache."""
        with self.lock:
            size_before = len(self.cache)
            self.cache.clear()
            logger.info(f"Cache CLEARED: removed {size_before} entries")
    
    def exists(self, key: str) -> bool:
        """
        Check if a key exists in the cache.
        
        Args:
            key: Cache key
            
        Returns:
            True if key exists, False otherwise
        """
        with self.lock:
            exists = key in self.cache
            logger.debug(f"Cache EXISTS: key={key}, exists={exists}")
            return exists
    
    def get_or_set(self, key: str, default: Any) -> Any:
        """
        Get value from cache or set default if not found.
        
        Args:
            key: Cache key
            default: Default value to set if key not found
            
        Returns:
            Cached value or default value
        """
        with self.lock:
            if key not in self.cache:
                self.cache[key] = default
                logger.debug(f"Cache GET_OR_SET: key={key} not found, setting default, cache_size={len(self.cache)}/{self.max_size}")
            else:
                logger.debug(f"Cache GET_OR_SET: key={key} found")
            return self.cache[key]
    
    def increment(self, key: str, amount: int = 1) -> int:
        """
        Increment a numeric value in the cache.
        
        Args:
            key: Cache key
            amount: Amount to increment by (default: 1)
            
        Returns:
            New value after increment
        """
        with self.lock:
            current = self.cache.get(key, 0)
            new_value = current + amount
            self.cache[key] = new_value
            logger.debug(f"Cache INCREMENT: key={key}, old_value={current}, new_value={new_value}, amount={amount}")
            return new_value
    
    def decrement(self, key: str, amount: int = 1) -> int:
        """
        Decrement a numeric value in the cache.
        
        Args:
            key: Cache key
            amount: Amount to decrement by (default: 1)
            
        Returns:
            New value after decrement
        """
        with self.lock:
            current = self.cache.get(key, 0)
            new_value = current - amount
            self.cache[key] = new_value
            logger.debug(f"Cache DECREMENT: key={key}, old_value={current}, new_value={new_value}, amount={amount}")
            return new_value
    
    def get_size(self) -> int:
        """
        Get the number of items currently in cache.
        
        Returns:
            Number of cached items
        """
        with self.lock:
            size = len(self.cache)
            logger.debug(f"Cache SIZE: {size}/{self.max_size}")
            return size
    
    def is_empty(self) -> bool:
        """
        Check if cache is empty.
        
        Returns:
            True if cache is empty, False otherwise
        """
        with self.lock:
            empty = len(self.cache) == 0
            logger.debug(f"Cache IS_EMPTY: {empty}")
            return empty
    
    def get_all_keys(self) -> list:
        """
        Get all keys in the cache.
        
        Returns:
            List of all cache keys
        """
        with self.lock:
            keys = list(self.cache.keys())
            logger.debug(f"Cache GET_ALL_KEYS: {len(keys)} keys found")
            return keys
    
    def close(self) -> None:
        """Close/cleanup the cache."""
        with self.lock:
            if self.cache:
                size = len(self.cache)
                self.cache.clear()
                self.cache = None
                logger.info(f"CacheManager closed: cleared {size} entries")


# Global cache manager instance
_cache_manager: Optional[CacheManager] = None


def get_cache_manager() -> CacheManager:
    """
    Get the global cache manager instance.
    
    Returns:
        The initialized cache manager
        
    Raises:
        RuntimeError: If cache manager hasn't been initialized
    """
    global _cache_manager
    if _cache_manager is None:
        logger.error("Cache manager not initialized. Call init_cache_manager() first.")
        raise RuntimeError("Cache manager not initialized. Call init_cache_manager() first.")
    return _cache_manager


def init_cache_manager(
    cache_type: Type[Cache] = TTLCache,
    max_size: int = 1000,
    ttl: int = 3600,
    **kwargs
) -> CacheManager:
    """
    Initialize the global cache manager.
    
    Args:
        cache_type: Type of cache to use
        max_size: Maximum number of items in cache
        ttl: Time-to-live in seconds
        **kwargs: Additional cache initialization arguments
        
    Returns:
        The initialized cache manager
    """
    global _cache_manager
    logger.info(f"Initializing global cache manager: type={cache_type.__name__}, max_size={max_size}, ttl={ttl}s")
    _cache_manager = CacheManager(
        cache_type=cache_type,
        max_size=max_size,
        ttl=ttl,
        **kwargs
    )
    logger.info("Global cache manager initialized successfully")
    return _cache_manager


def close_cache_manager() -> None:
    """Close the global cache manager."""
    global _cache_manager
    if _cache_manager:
        logger.info("Closing global cache manager")
        _cache_manager.close()
        _cache_manager = None
        logger.info("Global cache manager closed")

    """
    Centralized cache manager for handling different cache types.
    Thread-safe wrapper around cachetools caches.
    """
    
    def __init__(
        self,
        cache_type: Type[Cache] = TTLCache,
        max_size: int = 1000,
        ttl: int = 3600,
        **kwargs
    ):
        """
        Initialize the cache manager.
        
        Args:
            cache_type: Type of cache to use (TTLCache, LRUCache, etc.)
            max_size: Maximum number of items in cache
            ttl: Time-to-live in seconds (for TTLCache)
            **kwargs: Additional arguments for cache initialization
        """
        self.cache_type = cache_type
        self.max_size = max_size
        self.ttl = ttl
        self.lock = threading.RLock()
        self.cache: Optional[Cache] = None
        self._init_cache(**kwargs)
    
    def _init_cache(self, **kwargs):
        """Initialize the cache with appropriate parameters."""
        try:
            if self.cache_type == TTLCache:
                self.cache = TTLCache(maxsize=self.max_size, ttl=self.ttl)
            elif self.cache_type == LRUCache:
                self.cache = LRUCache(maxsize=self.max_size)
            else:
                # For custom cache types
                self.cache = self.cache_type(maxsize=self.max_size, **kwargs)
        except Exception as e:
            raise Exception(f"Failed to initialize cache: {str(e)}")
    
    def get(self, key: str) -> Optional[Any]:
        """
        Retrieve a value from the cache.
        
        Args:
            key: Cache key
            
        Returns:
            Cached value or None if not found
        """
        with self.lock:
            return self.cache.get(key)
    
    def set(self, key: str, value: Any) -> None:
        """
        Store a value in the cache.
        
        Args:
            key: Cache key
            value: Value to store
        """
        with self.lock:
            self.cache[key] = value
    
    def delete(self, key: str) -> bool:
        """
        Delete a value from the cache.
        
        Args:
            key: Cache key
            
        Returns:
            True if key existed, False otherwise
        """
        with self.lock:
            if key in self.cache:
                del self.cache[key]
                return True
            return False
    
    def clear(self) -> None:
        """Clear all entries from the cache."""
        with self.lock:
            self.cache.clear()
    
    def exists(self, key: str) -> bool:
        """
        Check if a key exists in the cache.
        
        Args:
            key: Cache key
            
        Returns:
            True if key exists, False otherwise
        """
        with self.lock:
            return key in self.cache
    
    def get_or_set(self, key: str, default: Any) -> Any:
        """
        Get value from cache or set default if not found.
        
        Args:
            key: Cache key
            default: Default value to set if key not found
            
        Returns:
            Cached value or default value
        """
        with self.lock:
            if key not in self.cache:
                self.cache[key] = default
            return self.cache[key]
    
    def increment(self, key: str, amount: int = 1) -> int:
        """
        Increment a numeric value in the cache.
        
        Args:
            key: Cache key
            amount: Amount to increment by (default: 1)
            
        Returns:
            New value after increment
        """
        with self.lock:
            current = self.cache.get(key, 0)
            new_value = current + amount
            self.cache[key] = new_value
            return new_value
    
    def decrement(self, key: str, amount: int = 1) -> int:
        """
        Decrement a numeric value in the cache.
        
        Args:
            key: Cache key
            amount: Amount to decrement by (default: 1)
            
        Returns:
            New value after decrement
        """
        with self.lock:
            current = self.cache.get(key, 0)
            new_value = current - amount
            self.cache[key] = new_value
            return new_value
    
    def get_size(self) -> int:
        """
        Get the number of items currently in cache.
        
        Returns:
            Number of cached items
        """
        with self.lock:
            return len(self.cache)
    
    def is_empty(self) -> bool:
        """
        Check if cache is empty.
        
        Returns:
            True if cache is empty, False otherwise
        """
        with self.lock:
            return len(self.cache) == 0
    
    def get_all_keys(self) -> list:
        """
        Get all keys in the cache.
        
        Returns:
            List of all cache keys
        """
        with self.lock:
            return list(self.cache.keys())
    
    def close(self) -> None:
        """Close/cleanup the cache."""
        with self.lock:
            if self.cache:
                self.cache.clear()
                self.cache = None


# Global cache manager instance
_cache_manager: Optional[CacheManager] = None


def get_cache_manager() -> CacheManager:
    """
    Get the global cache manager instance.
    
    Returns:
        The initialized cache manager
        
    Raises:
        RuntimeError: If cache manager hasn't been initialized
    """
    global _cache_manager
    if _cache_manager is None:
        raise RuntimeError("Cache manager not initialized. Call init_cache_manager() first.")
    return _cache_manager


def init_cache_manager(
    cache_type: Type[Cache] = TTLCache,
    max_size: int = 1000,
    ttl: int = 3600,
    **kwargs
) -> CacheManager:
    """
    Initialize the global cache manager.
    
    Args:
        cache_type: Type of cache to use
        max_size: Maximum number of items in cache
        ttl: Time-to-live in seconds
        **kwargs: Additional cache initialization arguments
        
    Returns:
        The initialized cache manager
    """
    global _cache_manager
    _cache_manager = CacheManager(
        cache_type=cache_type,
        max_size=max_size,
        ttl=ttl,
        **kwargs
    )
    return _cache_manager


def close_cache_manager() -> None:
    """Close the global cache manager."""
    global _cache_manager
    if _cache_manager:
        _cache_manager.close()
        _cache_manager = None
