#!/usr/bin/env python3
"""This module implements a LIFO cache"""
from base_caching import BaseCaching
from datetime import datetime


class LIFOCache(BaseCaching):
    """ LIFO cache system """
    timed_cache_data = {}

    def put(self, key, item):
        """ Puts key and item in cache dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.timed_cache_data[key] = datetime.now().strftime(
                "%m/%d/%Y %H:%M:%S:%f")
            if len(self.cache_data) > self.MAX_ITEMS:
                most_recent = sorted(self.timed_cache_data.values())[-2]
                for k, val in self.timed_cache_data.copy().items():
                    if val == most_recent:
                        del self.cache_data[k]
                        del self.timed_cache_data[k]
                        print(f"DISCARD: {k}")

    def get(self, key):
        """ Gets key from cache dictionary if it exists """
        return self.cache_data.get(key)
