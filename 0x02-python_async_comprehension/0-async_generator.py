#!/usr/bin/env python3
"""This module handles the basics of async comprehension"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """This function creates an async generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
