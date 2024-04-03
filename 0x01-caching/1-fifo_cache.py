#!/usr/bin/python3
"""
first in first out caching replacement policy
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """Initialize """

        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key
        """
        if key and item:

            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:

                for index, value in enumerate(self.cache_data.keys()):

                    if index == 0:
                        discarded = value

                print(f'DISCARDED: {discarded}')
                self.cache_data.pop(discarded)


    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """

        return self.cache_data.get(key)
