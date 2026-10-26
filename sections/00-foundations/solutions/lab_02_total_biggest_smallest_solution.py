"""
SOLUTION — Lab 0.02 Total, Biggest, Smallest
Time O(n), space O(1).

Key idea: start the running values from the first item, then walk the rest.
Starting from nums[0] avoids picking a "fake" starting value. The other good option is
float("-inf") for biggest and float("inf") for smallest.

Pitfall: starting biggest at 0 breaks on all-negative lists ([-3, -1, -7] would say 0).
"""
from typing import List, Tuple


def stats(nums: List[int]) -> Tuple[int, int, int]:
    total = 0
    biggest = nums[0]
    smallest = nums[0]
    for x in nums:
        total += x
        if x > biggest:
            biggest = x
        if x < smallest:
            smallest = x
    return total, biggest, smallest
