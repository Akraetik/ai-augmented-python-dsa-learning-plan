"""
SOLUTION — Lab 2.07 Trapping Rain Water, Two Pointers (LeetCode 42)
Time O(n). Space O(1).
Update both maxes with the current bars. The side with the smaller max has a known water level:
its own max is exact, and the other side has at least a taller bar. Add that side's water, move it inward.
"""
from typing import List


def trap(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    total = 0
    while left < right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])
        if left_max < right_max:
            total += left_max - height[left]
            left += 1
        else:
            total += right_max - height[right]
            right -= 1
    return total
