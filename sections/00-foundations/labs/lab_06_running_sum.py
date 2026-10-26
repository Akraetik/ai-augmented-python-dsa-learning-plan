"""
LAB 0.06 — Running Sum                                       Tier: Core
LeetCode 1480 (Easy) — https://leetcode.com/problems/running-sum-of-1d-array/
Pattern: prefix sum (a running total). Section 1 uses this idea a lot.
Lesson: 00.3

THE PROBLEM (in our words)
Return a new list where position i holds the total of everything from position 0 through position i.

RETURNS: List[int], same length as the input

EXAMPLES
  [3, 1, 4, 1]   ->  [3, 4, 8, 9]
  [5]            ->  [5]

CONSTRAINTS
  1 <= len(nums) <= 100,000

THINK ABOUT
  The tempting version: for each i, compute sum(nums[:i+1]). What's hidden inside that line?
  How can answer[i] reuse answer[i - 1]?
"""
from typing import List

# PLAN
# RETURNS:
# Tempting version + its real Big-O:
# Better idea + Big-O:


def running_sum(nums: List[int]) -> List[int]:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "running_sum"
CASES = [
    (([3, 1, 4, 1],), [3, 4, 8, 9], "example"),
    (([5],), [5], "one item"),
    (([1, -1, 1, -1],), [1, 0, 1, 0], "negatives"),
    (([0, 0, 0],), [0, 0, 0], "zeros"),
]
PERF = [("100,000 numbers", lambda: ([1] * 100_000,), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(running_sum)
