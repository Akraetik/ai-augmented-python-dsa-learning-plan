"""
SOLUTION — Lab 1.14 Trapping Rain Water (LeetCode 42)
Time O(n). Space O(n).

water[i] = min(tallest bar from 0..i, tallest bar from i..n-1) - height[i].
Including bar i in both maxes keeps the result >= 0 and makes edges hold 0 water automatically.

Two-pointer O(1)-space version (you'll do it in Section 02):
    left, right = 0, n - 1; left_max = right_max = 0; total = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left]); total += left_max - height[left]; left += 1
        else:
            right_max = max(right_max, height[right]); total += right_max - height[right]; right -= 1
"""
from typing import List


def trap(height: List[int]) -> int:
    n = len(height)
    max_left = [0] * n
    max_right = [0] * n
    best = 0
    for i in range(n):
        best = max(best, height[i])
        max_left[i] = best
    best = 0
    for i in range(n - 1, -1, -1):
        best = max(best, height[i])
        max_right[i] = best
    return sum(min(max_left[i], max_right[i]) - height[i] for i in range(n))
