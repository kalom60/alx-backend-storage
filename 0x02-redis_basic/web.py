#!/usr/bin/env python3
import redis
import requests
from typing import Callable
from functools import wraps


def access(method: Callable) -> Callable:
    """"""
    @wraps(method)
    def count(url: str) -> str:
        """"""
        redis_client = redis.Redis()
        if redis_client.get(f'count:{url}'):
            redis_client.incr(f'count:{url}')
            print(redis_client.get(f'count:{url}'))
        else:
            redis_client.setex(f'count:{url}', 10, 1)
            print(redis_client.get(f'count:{url}'))
    return count


@access
def get_page(url: str) -> str:
    """"""
    return requests.get(url)
