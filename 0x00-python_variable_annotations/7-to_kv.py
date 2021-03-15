#!/usr/bin/python3
"""This module implements a to_kv function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string and int/float and returns a tuple"""
    return (k, v ** 2)
