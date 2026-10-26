"""
LAB 2.03 — Two Sum II (Input Array Is Sorted)                Tier: Build
LeetCode 167 (Medium) — https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Lesson 2.1 · Pattern: opposite ends — too small moves left, too big moves right

THE PROBLEM (in our words)
numbers is sorted from small to big. Exactly one pair adds up to target.
Return the two positions as [i, j], 1-INDEXED (the first item is position 1), with i < j.
Use O(1) extra space: no dict this time.

RETURNS: List[int] of two 1-indexed positions   (M6: read that twice)

EXAMPLES
  [2, 7, 11, 15], target 9   ->  [1, 2]
  [2, 3, 4], target 6        ->  [1, 3]
  [-1, 0], target -1         ->  [1, 2]

CONSTRAINTS
  2 <= len(numbers) <= 30,000 (perf test: 300,000)

BEFORE YOU CODE
  Write the one-sentence reason it's safe to discard numbers[left] when the sum is too small.
"""
from typing import List

# PLAN
# RETURNS:
# Too small → move ___ because ___
# Too big → move ___ because ___
# Idea + Big-O (time and space):


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "two_sum_sorted"
CASES = [
    (([2, 7, 11, 15], 9), [1, 2], "example"),
    (([2, 3, 4], 6), [1, 3], "ends"),
    (([-1, 0], -1), [1, 2], "two items"),
    (([1, 2, 3, 4, 4, 9, 56, 90], 8), [4, 5], "duplicate values"),
    (([5, 25, 75], 100), [2, 3], "right side"),
    (([-10, -3, 0, 4, 8], -13), [1, 2], "negatives"),
]


def _big():
    n = 300_000
    nums = list(range(0, 2 * n, 2))
    return (nums, nums[-1] + nums[-2])      # the only pair is the last two


PERF = [("300,000 numbers, the only pair is at the end", _big, 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(two_sum_sorted)
