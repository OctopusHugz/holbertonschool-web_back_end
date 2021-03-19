#!/usr/bin/env python3
"""This module implements a basic cache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic cache system """
    def put(self, key, item):
        """ Puts key and item in cache dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Gets key from cache dictionary if it exists """
        return self.cache_data.get(key)
