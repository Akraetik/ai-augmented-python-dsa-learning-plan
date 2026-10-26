"""
SOLUTION — Lab 0.09 Two Sum (LeetCode 1)
Time O(n), space O(n).

Brute force: every pair, O(n^2).
Key idea: standing on value x, the partner I need is target - x. Keep a dict of
value -> index for everything I've already walked past. If the partner is in it, done.

Why check BEFORE adding x: so x can't pair with itself. [3, 3], target 6 works because
the first 3 is already stored when we stand on the second 3.
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    index_of = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in index_of:
            return [index_of[need], i]
        index_of[x] = i
    return []
