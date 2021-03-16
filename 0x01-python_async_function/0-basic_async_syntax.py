#!/usr/bin/env python3
"""This module focuses on asyncio basics"""
import asyncio
import random


async def wait_random(max_delay: int=10) -> float:
    """This async function awaits a random delay and returns its value"""
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
