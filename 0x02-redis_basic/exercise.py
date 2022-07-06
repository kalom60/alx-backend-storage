#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """init cache"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """write string data with random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
