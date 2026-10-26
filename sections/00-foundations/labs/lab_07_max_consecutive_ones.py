"""
LAB 0.07 — Max Consecutive Ones                              Tier: Core
LeetCode 485 (Easy) — https://leetcode.com/problems/max-consecutive-ones/
Pattern: running count that resets + running best
Lesson: 00.5

THE PROBLEM (in our words)
The list holds only 0s and 1s. Return the length of the longest unbroken run of 1s.

RETURNS: int

EXAMPLES
  [1, 1, 0, 1, 1, 1, 0]   ->  3
  [0, 0]                  ->  0

CONSTRAINTS
  1 <= len(nums) <= 100,000

THINK ABOUT
  You need two numbers: the run you're in right now, and the best run so far.
  What happens to each one when you hit a 0? When you hit a 1?
  Trace [1, 1, 1] carefully. Does your best get updated if the list ENDS on a 1?
"""
from typing import List

# PLAN
# RETURNS:
# Two variables I'll track:
# On a 1:
# On a 0:
# Edge cases:


def max_consecutive_ones(nums: List[int]) -> int:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "max_consecutive_ones"
CASES = [
    (([1, 1, 0, 1, 1, 1, 0],), 3, "example"),
    (([0, 0],), 0, "no ones"),
    (([1, 1, 1],), 3, "ends on a run"),
    (([1],), 1, "one item"),
    (([1, 0, 1, 0, 1],), 1, "alternating"),
    (([0, 1, 1, 0, 1, 1, 1, 1],), 4, "best run is last"),
]
PERF = [("100,000 items", lambda: (([1] * 999 + [0]) * 100,), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(max_consecutive_ones)
