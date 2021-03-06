#!/usr/bin/env python3
"""This module is working on duck typing"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Safely returns the first element if it exists"""
    if lst:
        return lst[0]
    else:
        return None
