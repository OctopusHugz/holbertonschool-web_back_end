#!/usr/bin/env python3
"""This module works on duck types"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This function returns the length of each element in a list as a tuple"""
    return [(i, len(i)) for i in lst]
