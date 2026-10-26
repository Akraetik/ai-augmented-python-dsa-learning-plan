"""
SOLUTION — Lab 0.07 Max Consecutive Ones (LeetCode 485)
Time O(n), space O(1).

Two running values: `current` (this run) and `best` (best run so far).
On a 1: current grows, and best takes the max right away.
On a 0: current resets to 0.

Pitfall: updating best only when you hit a 0 misses a run that ends the list. Update on every 1.
"""
from typing import List


def max_consecutive_ones(nums: List[int]) -> int:
    best = 0
    current = 0
    for x in nums:
        if x == 1:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best
