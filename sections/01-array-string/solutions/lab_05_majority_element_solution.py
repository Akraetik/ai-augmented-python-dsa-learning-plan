"""
SOLUTION — Lab 1.05 Majority Element (LeetCode 169)

Way 1, counting:  O(n) time, O(n) space.
    from collections import Counter
    return Counter(nums).most_common(1)[0][0]

Way 2, sorting:   O(n log n). The majority covers more than half, so it must sit at the middle index.
    return sorted(nums)[len(nums) // 2]

Way 3, Boyer–Moore voting (below): O(n) time, O(1) space.
Each non-majority item can cancel at most one majority item. The majority has more items than all
others combined, so it survives as the candidate. Only valid because a majority is guaranteed.
"""
from typing import List


def majority_element(nums: List[int]) -> int:
    candidate, count = None, 0
    for x in nums:
        if count == 0:
            candidate = x
        count += 1 if x == candidate else -1
    return candidate
