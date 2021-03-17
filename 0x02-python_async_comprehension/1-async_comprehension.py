#!/usr/bin/env python3
"""This module handles the basics of async comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """This function creates an async generator"""
    return [i async for i in async_generator()]
