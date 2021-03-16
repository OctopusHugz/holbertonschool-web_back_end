#!/usr/bin/env python3
"""This module focuses on asyncio basics of concurrent coroutines"""
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with specified max_delay"""
    delay_list: List[float] = []
    for _ in range(0, n):
        random_delay: int = await wait_random(max_delay)
        delay_list.append(random_delay)
    return delay_list
