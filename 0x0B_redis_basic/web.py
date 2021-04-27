#!/usr/bin/env python3
""" This module implements an expiring web cache and tracker """
from functools import wraps
from typing import Callable
import redis
import requests

r = redis.Redis()
# r.flushdb()


def count_cache(method: Callable) -> Callable:
    """ Tracks how many times a particular URL was accessed """

    @wraps(method)
    def wrapper(*args):
        """ Wrapper func for get_page """
        key = f"count:{args[0]}"
        r.incr(key, 1)
        r.setex("result", 10, r.get(key))
        return method(*args)
    return wrapper


@count_cache
def get_page(url: str) -> str:
    """ Uses requests to obtain and return the HTML content of URL """
    response = requests.get(url)
    return response.text
