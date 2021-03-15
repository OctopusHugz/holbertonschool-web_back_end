#!/usr/bin/env python3
"""This module is working on duck typing"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """Safely fetches value from a dictionary if key exists in dct"""
    if key in dct:
        return dct[key]
    else:
        return default
