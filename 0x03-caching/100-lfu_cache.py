#!/usr/bin/env python3
"""This module implements a LFU cache"""
from base_caching import BaseCaching
from datetime import datetime


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
            self.cache_data[key] = item
            if self.ccd.get(key) is None:
                self.ccd[key] = 1
            else:
                self.ccd[key] += 1
            self.tcd[key] = datetime.now().strftime("%m/%d/%Y %H:%M:%S:%f")
            if len(self.cache_data) > self.MAX_ITEMS:
                lowest_count = min(self.ccd.values())
                if lowest_count == 1 and self.ccd[key] == 1:
                    lowest_list = sorted(list(self.ccd.values()))
                    lowest_list.pop(0)
                    lowest_count = lowest_list[0]
                self.lfk = {}
                for keys, vals in self.ccd.copy().items():
                    if vals == lowest_count:
                        self.lfk[keys] = self.tcd.get(keys)
                lfru_key = min(self.lfk)
                del self.cache_data[lfru_key]
                del self.tcd[lfru_key]
                del self.ccd[lfru_key]
                print(f"DISCARD: {lfru_key}")
                # else:
                #     for k, v in self.ccd.copy().items():
                #         if v == lowest_count:
                #             del self.cache_data[k]
                #             del self.tcd[k]
                #             del self.ccd[k]
                #             print(f"DISCARD: {k}")

    def get(self, key):
        """ Gets key from cache dictionary if it exists """
        value = self.cache_data.get(key)
        if value is not None:
            if self.ccd.get(key) is None:
                self.ccd[key] = 1
            else:
                self.ccd[key] += 1
            self.tcd[key] = datetime.now().strftime("%m/%d/%Y %H:%M:%S:%f")
        return value
