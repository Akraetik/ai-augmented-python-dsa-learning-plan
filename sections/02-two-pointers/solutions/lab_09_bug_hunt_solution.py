"""
SOLUTION — Lab 2.09 Bug Hunt: Two Sum II

The four bugs:
1. right = len(numbers) is one past the end.                   -> M5. Fix: len(numbers) - 1
2. return [left, right] is 0-indexed; the problem wants 1.      -> M6. Fix: [left + 1, right + 1]
3. Too small moves RIGHT (makes the sum smaller still).         -> NEW: moving the wrong pointer.
   Fix: too small → left += 1; too big → right -= 1.
   Check: "Which pointer makes the sum go the way I need?"  Candidate M8.
4. left + 1 is never saved.                                      -> M4. Fix: left += 1 (now in the other branch)
"""
from typing import List


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []
