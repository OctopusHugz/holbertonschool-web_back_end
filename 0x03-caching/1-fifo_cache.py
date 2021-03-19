#!/usr/bin/env python3
"""This module implements a basic cache"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache system """
    cache_list = []

    def put(self, key, item):
        """ Puts key and item in cache dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.cache_list:
                self.cache_list.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                popped_key = self.cache_list.pop(0)
                print(f"DISCARD: {popped_key}")
                del self.cache_data[popped_key]

    def get(self, key):
        """ Gets key from cache dictionary if it exists """
        return self.cache_data.get(key)
