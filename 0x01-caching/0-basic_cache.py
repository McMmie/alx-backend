#!/usr/bin/python3
"""
basic chaching
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """Initialize """

        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """

        return self.cache_data.get(key)
