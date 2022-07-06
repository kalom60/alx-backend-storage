#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import redis
import requests
from typing import Callable
from functools import wraps


redis_client = redis.Redis()


def access(method: Callable) -> Callable:
    """track how many times a particular URL was accessed"""
    @wraps(method)
    def count(url: str) -> str:
        """count how many times a request has been made"""
        redis_client.incr(f'count:{url}')
        if redis_client.get(f'count:{url}'):
            print((redis_client.get(f'count:{url}')).decode('utf8'))
        result = method(url)
        redis_client.set(f'count:{url}', 1)
        redis_client.setex(f'result:{url}', 10, result)
        print((redis_client.get(f'count:{url}')).decode('utf8'))
    return count


@access
def get_page(url: str) -> str:
    """call a request"""
    return requests.get(url).text


get_page('http://slowwly.robertomurray.co.uk')
get_page('http://slowwly.robertomurray.co.uk')
get_page('http://slowwly.robertomurray.co.uk')
get_page('http://slowwly.robertomurray.co.uk')
get_page('http://slowwly.robertomurray.co.uk')
