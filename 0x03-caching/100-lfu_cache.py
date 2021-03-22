#!/usr/bin/env python3
"""This module implements a LFU cache"""
from base_caching import BaseCaching
from datetime import datetime
now = datetime.now()


class LFUCache(BaseCaching):
    """ LFU cache system """
    # timed_cache_data
    tcd = {}
    # counted_cache_data
    ccd = {}
    # least_frequent_keys
    lfk = {}

    def put(self, key, item):
        """ Puts key and item in cache dictionary """
        if key is not None and item is not None:
            if len(self.cache_data) == self.MAX_ITEMS:
                lowest_count = min(self.ccd.values())
                if self.ccd.get(key) == lowest_count:
                    self.cache_data[key] = item
                    self.ccd[key] += 1
                    self.tcd[key] = now.strftime("%m/%d/%Y %H:%M:%S:%f")
                    return
                self.lfk = {}
                for keys, vals in self.ccd.copy().items():
                    if vals == lowest_count:
                        self.lfk[keys] = self.tcd.get(keys)
                min_value = min(self.lfk.values())
                for k, v in self.lfk.items():
                    if v == min_value:
                        lfru_key = k
                        break
                del self.cache_data[lfru_key]
                del self.tcd[lfru_key]
                del self.ccd[lfru_key]
                print(f"DISCARD: {lfru_key}")

            self.cache_data[key] = item
            if self.ccd.get(key) is None:
                self.ccd[key] = 1
            else:
                self.ccd[key] += 1
            self.tcd[key] = now.strftime("%m/%d/%Y %H:%M:%S:%f")

    def get(self, key):
        """ Gets key from cache dictionary if it exists """
        value = self.cache_data.get(key)
        if value is not None:
            if self.ccd.get(key) is None:
                self.ccd[key] = 1
            else:
                self.ccd[key] += 1
            self.tcd[key] = now.strftime("%m/%d/%Y %H:%M:%S:%f")
        return value
