"""
SOLUTION — Lab 1.01 Merge Sorted Array (LeetCode 88)
Time O(m + n). Space O(1).

Fill from the back. The end of nums1 is empty space, so writing there never destroys unread values.
Each step: compare the last unplaced item of each list, place the bigger one at `write`, step left.

When nums2 runs out first: done. nums1's remaining items are already in place.
When nums1 runs out first: copy the rest of nums2 in. The `while p2 >= 0` loop handles both cases.

Common bug: `while p1 >= 0 and p2 >= 0` and then forgetting to copy leftover nums2.
"""
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    p1, p2, write = m - 1, n - 1, m + n - 1
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[write] = nums1[p1]
            p1 -= 1
        else:
            nums1[write] = nums2[p2]
            p2 -= 1
        write -= 1
