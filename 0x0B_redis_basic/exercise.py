#!/usr/bin/env python3
""" This module creates a Cache class and interacts with Redis """
from typing import Callable, Union
from redis import Redis
from uuid import uuid4


class Cache():
    """ This is an instance of the Cache class """

    def __init__(self) -> None:
        """ Creates an instance of the Cache class """
        self._redis = Redis()
        self._redis.flushdb()

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
