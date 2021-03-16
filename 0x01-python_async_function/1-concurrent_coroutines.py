#!/usr/bin/env python3
"""This module focuses on asyncio basics of concurrent coroutines"""
import asyncio
from typing import Any, List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with specified max_delay"""
    delay_list: List[float] = []
    tasks: List[int] = []
    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    for res in asyncio.as_completed(tasks):
        completed = await res
        delay_list.append(completed)
    return delay_list
