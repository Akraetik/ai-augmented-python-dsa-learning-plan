"""
SOLUTION — Lab 1.02 Remove Element (LeetCode 27)
Time O(n). Space O(1).
Keep rule: the item is not val.

Alternative when order doesn't matter: swap unwanted items with the end and shrink.
Fewer writes when val is rare. LeetCode accepts it; these tests check order, so use the write pointer.
"""
from typing import List


def remove_element(nums: List[int], val: int) -> int:
    write = 0
    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]
            write += 1
    return write
