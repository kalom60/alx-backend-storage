#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """init cache"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """write string data with random key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Optional[Callable]) -> Union[str, bytes, int, float]:
        """Get Data from redis"""
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """get string value from redis"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """get int value from redis"""
        return self.get(key, lambda x: int(x))
