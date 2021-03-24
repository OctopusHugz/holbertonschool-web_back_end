#!/usr/bin/env python3
""" This module creates a simple helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Returns a tuple of size two containing a start index and an end index"""
    return ((page - 1) * page_size, page * page_size)
