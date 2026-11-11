"""
SOLUTION — Lab 3.01 Maximum Average Subarray I (LeetCode 643)
Time O(n). Space O(1).
Build the first window once. Each slide: add nums[right], subtract nums[right - k].
Track the best SUM; divide once at the end (same answer, fewer float operations).
"""
from typing import List


def find_max_average(nums: List[int], k: int) -> float:
    window = sum(nums[:k])
    best = window
    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]
        best = max(best, window)
    return best / k
