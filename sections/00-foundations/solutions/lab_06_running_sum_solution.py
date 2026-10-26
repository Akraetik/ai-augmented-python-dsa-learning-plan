"""
SOLUTION — Lab 0.06 Running Sum (LeetCode 1480)
Time O(n), space O(n) for the output.

Tempting version: [sum(nums[:i+1]) for i in range(n)] — the slice and the sum are both O(i),
so the whole thing is O(n^2).

Key idea: each answer is the previous answer plus one new number. Keep a running total.
This is the PREFIX SUM idea. In Section 1 it powers Product of Array Except Self.
"""
from typing import List


def running_sum(nums: List[int]) -> List[int]:
    out = []
    total = 0
    for x in nums:
        total += x
        out.append(total)
    return out
