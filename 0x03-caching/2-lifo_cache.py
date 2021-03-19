#!/usr/bin/env python3
"""This module implements a LIFO cache"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO cache system """
    cache_list = []

    def put(self, key, item):
        """ Puts key and item in cache dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.cache_list:
                old_key_index = self.cache_list.index(key)
                self.cache_list.pop(old_key_index)
            self.cache_list.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                popped_key = self.cache_list.pop(3)
                print(f"DISCARD: {popped_key}")
                del self.cache_data[popped_key]

    def get(self, key):
        """ Gets key from cache dictionary if it exists """
        return self.cache_data.get(key)
