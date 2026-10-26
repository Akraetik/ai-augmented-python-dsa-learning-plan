"""
SOLUTION — Lab 1.04 Remove Duplicates from Sorted Array II (LeetCode 80)
Time O(n). Space O(1).

Keep rule: keep the item if fewer than 2 have been kept, OR it differs from the item TWO kept slots back.
If nums[read] == nums[write - 2], then (because sorted) nums[write - 1] is the same value too,
so this would be a third copy.

General form, allowing each value k times:
    if write < k or nums[read] != nums[write - k]: keep
Lab 03 is k = 1.
"""
from typing import List


def remove_duplicates_ii(nums: List[int]) -> int:
    write = 0
    for read in range(len(nums)):
        if write < 2 or nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1
    return write
