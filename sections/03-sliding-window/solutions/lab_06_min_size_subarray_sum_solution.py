"""
SOLUTION — Lab 3.06 Minimum Size Subarray Sum (LeetCode 209)
Time O(n). Space O(1).
Shortest-valid template: grow; while the sum is big enough, record, then shrink.
Only works because every number is positive (growing raises the sum, shrinking lowers it).
"""
from typing import List


def min_sub_array_len(target: int, nums: List[int]) -> int:
    left = 0
    total = 0
    best = float("inf")
    for right, x in enumerate(nums):
        total += x
        while total >= target:
            best = min(best, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if best == float("inf") else best
