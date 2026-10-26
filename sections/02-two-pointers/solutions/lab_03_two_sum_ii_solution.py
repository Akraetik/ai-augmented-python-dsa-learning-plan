"""
SOLUTION — Lab 2.03 Two Sum II (LeetCode 167)
Time O(n). Space O(1).
Too small: numbers[right] is the biggest partner left, and it still isn't enough,
so numbers[left] has no partner — discard it (left += 1). Too big: mirror argument.
Return 1-indexed positions.
"""
from typing import List


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        if total < target:
            left += 1
        else:
            right -= 1
    return []
