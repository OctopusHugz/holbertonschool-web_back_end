#!/usr/bin/env python3
"""This module handles the basics of async comprehension"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """This function creates an async generator"""
    return [i async for i in async_generator()]
