#!/usr/bin/env python3
"""This module implements a LFU cache"""
from base_caching import BaseCaching
from datetime import datetime


class LFUCache(BaseCaching):
    """ LFU cache system """
    timed_cache_data = {}
    counted_cache_data = {}
    least_frequent_keys = {}

    def put(self, key, item):
        """ Puts key and item in cache dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if self.counted_cache_data.get(key) is None:
                self.counted_cache_data[key] = 1
            else:
                self.counted_cache_data[key] += 1
            self.timed_cache_data[key] = datetime.now().strftime(
                "%m/%d/%Y %H:%M:%S:%f")
            if len(self.cache_data) > self.MAX_ITEMS:
                # lowest_count = min(self.counted_cache_data, key=lambda k: self.counted_cache_data[k])
                lowest_count = min(self.counted_cache_data.values())
                if lowest_count == 1 and self.counted_cache_data[key] == 1:
                    lowest_list = sorted(list(self.counted_cache_data.values()))
                    lowest_list.pop(0)
                    lowest_count = lowest_list[0]
                least_used_count = list(self.counted_cache_data.values()).count(lowest_count)
                if least_used_count > 1:
                    self.least_frequent_keys = {}
                    for keys, vals in self.counted_cache_data.copy().items():
                        if vals == lowest_count:
                            self.least_frequent_keys[keys] = self.timed_cache_data.get(keys)
                    lfru_key = min(self.least_frequent_keys)
                    del self.cache_data[lfru_key]
                    del self.timed_cache_data[lfru_key]
                    del self.counted_cache_data[lfru_key]
                    print(f"DISCARD: {lfru_key}")
                else:
                    for k, v in self.counted_cache_data.copy().items():
                        if v == lowest_count:
                            del self.cache_data[k]
                            del self.timed_cache_data[k]
                            del self.counted_cache_data[k]
                            print(f"DISCARD: {k}")

    def get(self, key):
        """ Gets key from cache dictionary if it exists """
        value = self.cache_data.get(key)
        if value is not None:
            if self.counted_cache_data.get(key) is None:
                self.counted_cache_data[key] = 1
            else:
                self.counted_cache_data[key] += 1
            self.timed_cache_data[key] = datetime.now().strftime(
                "%m/%d/%Y %H:%M:%S:%f")
        return value
