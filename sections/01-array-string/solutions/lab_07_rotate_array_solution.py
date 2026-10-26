"""
SOLUTION — Lab 1.07 Rotate Array (LeetCode 189)

Reduce k first: k %= n. Rotating by n changes nothing.

Way 1 (O(n) space):
    rotated = [0] * n
    for i in range(n): rotated[(i + k) % n] = nums[i]
    nums[:] = rotated            # slice-assign so the caller's list changes

Way 2 (below, O(1) space): reverse all, reverse the first k, reverse the rest.
"""
from typing import List


def _reverse(nums: List[int], left: int, right: int) -> None:
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n
    _reverse(nums, 0, n - 1)
    _reverse(nums, 0, k - 1)
    _reverse(nums, k, n - 1)
