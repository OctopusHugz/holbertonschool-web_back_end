#!/usr/bin/env python3
"""This module implements a make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float and returns a function that multiplies a float by the
parameter multiplier"""
    def new_func(new_multiplier: float) -> float:
        """Takes a float and multiplies it by multiplier"""
        return multiplier * new_multiplier
    return new_func
