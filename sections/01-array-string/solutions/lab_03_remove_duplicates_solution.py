"""
SOLUTION — Lab 1.03 Remove Duplicates from Sorted Array (LeetCode 26)
Time O(n). Space O(1).

Keep rule: the item differs from the last KEPT item, nums[write - 1].
Comparing with nums[read - 1] also works here, because the input is sorted. But only the
nums[write - 1] form generalizes to lab 04 ("look back k kept slots").
"""
from typing import List


def remove_duplicates(nums: List[int]) -> int:
    write = 0
    for read in range(len(nums)):
        if write == 0 or nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write
