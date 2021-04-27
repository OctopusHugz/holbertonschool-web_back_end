#!/usr/bin/env python3
""" This module creates a Cache class and interacts with Redis """
from functools import wraps
from typing import Callable, Union
from uuid import uuid4
import redis


def replay(func: Callable) -> None:
    """ Displays the history of calls of a particular function """
    self = func.__self__
    input_list_key = func.__qualname__ + ":inputs"
    output_list_key = func.__qualname__ + ":outputs"
    call_count = self._redis.get(func.__qualname__).decode()
    inputs = self._redis.lrange(input_list_key, 0, -1)
    outputs = self._redis.lrange(output_list_key, 0, -1)
    print(f"{func.__qualname__} was called {call_count} times:")
    for input, output in zip(inputs, outputs):
        input_str = f"{func.__qualname__}(*{input.decode()}) -> "
        output_str = f"{output.decode()}"
        print(input_str + output_str)


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

    def __init__(self):
        """ Creates an instance of the Cache class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generates a random key with uuid and stores data in Redis using
        that random key """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        """ Gets the value of key from Redis, if it exists """
        if fn is not None:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """ Gets a bytes string and typecasts return to a str """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """ Gets a bytes string and typecasts return to an int """
        return self.get(key, int)
