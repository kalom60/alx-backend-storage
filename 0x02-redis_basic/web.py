#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import redis
import requests
from typing import Callable
from functools import wraps


def access(method: Callable) -> Callable:
    """track how many times a particular URL was accessed"""
    @wraps(method)
    def count(url: str) -> str:
        """count how many times a request has been made"""
        redis_client = redis.Redis()
        if redis_client.get(f'count:{url}'):
            redis_client.incr(f'count:{url}')
            return (redis_client.get(f'count:{url}')).decode('utf8')
        method(url)
        redis_client.setex(f'count:{url}', 10, 1)
        return (redis_client.get(f'count:{url}')).decode('utf8')
    return count


@access
def get_page(url: str) -> str:
    """call a request"""
    return requests.get(url)
