#!/usr/bin/env python3
"""The least Frequently Used caching module.
"""

from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """This represents object that allows storing and
    retrieving items from a dictionary with LFU
    removal mechanism when limit is reached.
    """

    def __init__(self):
        """This initializes cache."""

        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def __reorder_items(self, mru_key):
        """This reorders items in this cache based on most
        recently used item.
        """
        max_positions = []
        mru_freq = 0
        mru_pos = 0
        ins_pos = 0
        for j, key_freq in enumerate(self.keys_freq):
            if key_freq[0] == mru_key:
                mru_freq = key_freq[1] + 1
                mru_pos = j
                break
            elif len(max_positions) == 0:
                max_positions.append(j)
            elif key_freq[1] < self.keys_freq[max_positions[-1]][1]:
                max_positions.append(j)
        max_positions.reverse()
        for pos in max_positions:
            if self.keys_freq[pos][1] > mru_freq:
                break
            ins_pos = pos
        self.keys_freq.pop(mru_pos)
        self.keys_freq.insert(ins_pos, [mru_key, mru_freq])

    def put(self, key, item):
        """This adds an item in the cache."""

        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = len(self.keys_freq)
            for j, key_freq in enumerate(self.keys_freq):
                if key_freq[1] == 0:
                    ins_index = j
                    break
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """This retrieves item by key."""
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)

        return self.cache_data.get(key, None)
