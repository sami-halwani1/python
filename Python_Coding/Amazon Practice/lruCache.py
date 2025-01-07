from collections import OrderedDict
import random
"""
Design a datastructure that follows tthe contracts of a least recently used LRU cache

Implement the LURCache class:
    - LRUCache(int capacity) intialize theLRU cache with positive size capacity
    - int get(int key) Return the value of the key if the key exists, otherwise return -1
    - void put(int key, int value) Update the value of the key if the key exists. Otherwise,
    add the key-value pair to the cache. if the number of keys exceeds the capacity from this
    operation, evict the least recently used key.

The function get and put much each run at 0(1) average time complexity.
"""

class LRUCache(OrderedDict):
    
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int )-> int:
        if key in self:
            self.move_to_end(key)
            return self[key]
        else:
            return -1

    def put(self, key:int, value: int) -> None:
        self[key] = value

        if len(self) > self.capacity:
            self.popitem(last=False)

        self.move_to_end(key)
        
