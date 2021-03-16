#!/usr/bin/env python3
"""This module focuses on asyncio basics of concurrent coroutines"""
import asyncio
from typing import Any, List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with specified max_delay"""
    delay_list: List[float] = []
    tasks: List[Any] = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    for res in asyncio.as_completed(tasks):
        completed = await res
        delay_list.append(completed)
    return delay_list
