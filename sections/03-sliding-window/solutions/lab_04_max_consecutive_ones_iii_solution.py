"""
SOLUTION — Lab 3.04 Max Consecutive Ones III (LeetCode 1004)
Time O(n). Space O(1).
Restated: the longest window with at most k zeros. Count zeros in the window; shrink while zeros > k.
"""
from typing import List


def longest_ones(nums: List[int], k: int) -> int:
    left = 0
    zeros = 0
    best = 0
    for right, x in enumerate(nums):
        if x == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
