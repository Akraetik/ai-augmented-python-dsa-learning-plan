"""
SOLUTION — Lab 2.04 Squares of a Sorted Array (LeetCode 977)
Way 1: sorted(x * x for x in nums)     O(n log n)
Way 2 (below): the biggest squares sit at the two ends. Compare absolute values,
write the bigger square into the last open slot, move that pointer inward. O(n).
"""
from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    n = len(nums)
    out = [0] * n
    left, right = 0, n - 1
    for write in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            out[write] = nums[left] * nums[left]
            left += 1
        else:
            out[write] = nums[right] * nums[right]
            right -= 1
    return out
