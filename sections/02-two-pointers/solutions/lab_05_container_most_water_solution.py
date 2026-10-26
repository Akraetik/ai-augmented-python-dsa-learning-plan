"""
SOLUTION — Lab 2.05 Container With Most Water (LeetCode 11)
Time O(n). Space O(1).
Every container that keeps the shorter line and moves the other end inward is narrower and no taller,
so it can't beat the current area. The shorter line is finished: move it.
"""
from typing import List


def max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        h = min(height[left], height[right])
        best = max(best, (right - left) * h)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best
