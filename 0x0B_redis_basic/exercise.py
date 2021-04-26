#!/usr/bin/env python3
""" This module creates a Cache class and interacts with Redis """
from typing import Union
from redis import Redis
from uuid import uuid4


class Cache(object):
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
