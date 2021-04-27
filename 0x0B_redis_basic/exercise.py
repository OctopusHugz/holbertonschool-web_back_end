#!/usr/bin/env python3
""" This module creates a Cache class and interacts with Redis """
from functools import wraps
from redis import Redis
from typing import Callable, Union
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """ Counts how many times methods of Cache class are called """
    @wraps(method)
    def wrapper(self, *args) -> bytes:
        """ This is wrapper function for count_calls method """
        key = method.__qualname__
        self._redis.incr(key, 1)
        return method(self, *args)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Stores the history of inputs and outputs for a particular function """
    input_list_key = method.__qualname__ + ":inputs"
    output_list_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args) -> bytes:
        """ This is wrapper function for call_history method """
        self._redis.rpush(input_list_key, str(args))
        output = method(self, *args)
        self._redis.rpush(output_list_key, output)
        return output
    return wrapper


class Cache():
    """ This is an instance of the Cache class """

    def __init__(self) -> None:
        """ Creates an instance of the Cache class """
        self._redis = Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generates a random key with uuid and stores data in Redis using
        that random key """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, None]:
        """ Gets the value of key from Redis, if it exists """
        if fn is not None:
            value = fn(self._redis.get(key))
        else:
            value = self._redis.get(key)
        if value is None:
            return "(nil)"
        return value
