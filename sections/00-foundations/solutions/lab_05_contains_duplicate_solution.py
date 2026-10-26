"""
SOLUTION — Lab 0.05 Contains Duplicate (LeetCode 217)
Time O(n), space O(n).

Brute force: compare every pair. O(n^2). Fails the perf test.
Sort first: O(n log n), then check neighbors. Works, uses O(1) extra if you sort in place.
Set: O(n). The standard answer.

One-liner, also O(n):  return len(set(nums)) != len(nums)
The loop version can stop early when it finds a duplicate. The one-liner always builds the whole set.
"""
from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
