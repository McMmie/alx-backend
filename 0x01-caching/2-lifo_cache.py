#!/usr/bin/python3
"""
last in first out caching replacement policy
"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """Initialize """

        super().__init__()
        self.order = deque()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key
        """
        if key and item:

            self.cache_data[key] = item
            self.order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:

                for index, value in enumerate(self.cache_data.keys()):
                    if index == 3:
                        discarded = value

                print(f'DISCARDED: {discarded}')
                self.cache_data.pop(discarded)

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """

        return self.cache_data.get(key)
