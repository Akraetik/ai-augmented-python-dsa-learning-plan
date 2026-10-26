"""
LAB 2.04 — Squares of a Sorted Array                         Tier: Core
LeetCode 977 (Easy) — https://leetcode.com/problems/squares-of-a-sorted-array/
(Extra rep: not on the Top 150, but a classic warm-up for this pattern.)
Lesson 2.1 · Pattern: opposite ends, fill the output from the back

THE PROBLEM (in our words)
nums is sorted and may include negatives. Return a new list of the squares, sorted small to big.

RETURNS: List[int]

EXAMPLES
  [-4, -1, 0, 3, 10]   ->  [0, 1, 9, 16, 100]
  [-7, -3, 2, 3, 11]   ->  [4, 9, 9, 49, 121]

CONSTRAINTS
  1 <= len(nums) <= 10,000 (perf test: 300,000)

DO IT TWICE
  1. Square, then sorted(). Big-O?
  2. O(n): where do the BIGGEST squares sit in a sorted list with negatives? Fill the answer from the back.
"""
from typing import List

# PLAN
# RETURNS:
# Where the biggest squares are:
# Way 2 steps:


def sorted_squares(nums: List[int]) -> List[int]:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "sorted_squares"
CASES = [
    (([-4, -1, 0, 3, 10],), [0, 1, 9, 16, 100], "example"),
    (([-7, -3, 2, 3, 11],), [4, 9, 9, 49, 121], "example 2"),
    (([1],), [1], "one item"),
    (([-5, -3, -1],), [1, 9, 25], "all negative"),
    (([0, 2],), [0, 4], "no negatives"),
    (([-2, -2, 2, 2],), [4, 4, 4, 4], "mirror values"),
]
PERF = [("300,000 items", lambda: (list(range(-150_000, 150_000)),), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(sorted_squares)
