#!/usr/bin/env python3
"""This module implements a LRU cache"""
from base_caching import BaseCaching
from datetime import datetime


class LRUCache(BaseCaching):
    """ LRU cache system """
    timed_cache_data = {}

    def put(self, key, item):
        """ Puts key and item in cache dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.timed_cache_data[key] = datetime.now().strftime(
                "%m/%d/%Y %H:%M:%S:%f")
            least_recent = min(self.timed_cache_data.values())
            if len(self.cache_data) > self.MAX_ITEMS:
                for k, val in self.timed_cache_data.copy().items():
                    if val == least_recent:
                        del self.cache_data[k]
                        del self.timed_cache_data[k]
                        print(f"DISCARD: {k}")

    def get(self, key):
        """ Gets key from cache dictionary if it exists """
        value = self.cache_data.get(key)
        if value is not None:
            self.timed_cache_data[key] = datetime.now().strftime(
                "%m/%d/%Y %H:%M:%S:%f")
        return value
