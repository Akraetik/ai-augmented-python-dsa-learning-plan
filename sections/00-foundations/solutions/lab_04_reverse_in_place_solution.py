"""
SOLUTION — Lab 0.04 Reverse a List In Place
Time O(n), space O(1).

Key idea: two pointers. Swap the outside pair, step both inward, stop when they meet or cross.
`while left < right` handles odd lengths: the middle item never moves, which is correct.

Pitfall (M5): `while left <= right` also works but swaps the middle with itself. Harmless here,
but in other problems "<=" vs "<" matters. Trace both lengths every time.
"""
from typing import List


def reverse_in_place(nums: List[int]) -> None:
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
