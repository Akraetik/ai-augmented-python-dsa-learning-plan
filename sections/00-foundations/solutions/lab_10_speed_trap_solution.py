"""
SOLUTION — Lab 0.10 Speed Trap
Slow version: O(len(a) * len(b)) because `x in a` scans the whole LIST every time.
Fix: turn a into a set once. Then each `in` is O(1).
New time O(len(a) + len(b)), space O(len(a)).
"""
from typing import List


def count_common(a: List[int], b: List[int]) -> int:
    in_a = set(a)
    count = 0
    for x in b:
        if x in in_a:
            count += 1
    return count
