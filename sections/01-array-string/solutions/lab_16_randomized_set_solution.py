"""
SOLUTION — Lab 1.16 Insert Delete GetRandom O(1) (LeetCode 380)
All operations O(1) average. Space O(n).

values: list of members (random.choice needs indexing)
index_of: dict value -> its position in values (O(1) lookup)

Remove: move the LAST value into the removed value's slot, fix that value's index, pop the end,
then delete the removed value from the dict. If the removed value IS the last one, the steps still
work: it overwrites itself, then gets popped and deleted.
"""
import random


class RandomizedSet:
    def __init__(self):
        self.values = []
        self.index_of = {}

    def insert(self, val: int) -> bool:
        if val in self.index_of:
            return False
        self.index_of[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_of:
            return False
        i = self.index_of[val]
        last = self.values[-1]
        self.values[i] = last
        self.index_of[last] = i
        self.values.pop()
        del self.index_of[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
