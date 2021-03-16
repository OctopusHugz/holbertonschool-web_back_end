#!/usr/bin/env python3
"""This module measures the runtime of the wait_n function"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay)"""
    start_time: float = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(wait_n(n, max_delay))
    loop.close()
    end_time: float = time.time()
    return (end_time - start_time) / n
