#!/usr/bin/env python3
""" This module implements an expiring web cache and tracker """
from functools import wraps
from redis import Redis
from typing import Callable
import requests

r = Redis()
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
def get_page(url: str):
    """ Uses requests to obtain and return the HTML content of URL """
    # track how many times a particular URL was accessed in the key
    # and cache the result with an expiration time of 10 seconds
    response = requests.get(url)
    return response.text


# get_page("http://www.google.com")
