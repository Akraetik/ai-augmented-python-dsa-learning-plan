"""
LAB 3.01 — Maximum Average Subarray I                        Tier: Core
LeetCode 643 (Easy) — https://leetcode.com/problems/maximum-average-subarray-i/
(Extra rep: not on the Top 150. The cleanest fixed-window warm-up.)
Lesson 3.1 · Pattern: fixed window — add the entering item, remove the leaving item

THE PROBLEM (in our words)
Find the k items in a row with the biggest average. Return that average.

RETURNS: float

EXAMPLES
  nums = [1, 12, -5, -6, 50, 3], k = 4   ->  12.75   (12 - 5 - 6 + 50 = 51, 51 / 4)
  nums = [5], k = 1                      ->  5.0

CONSTRAINTS
  1 <= k <= len(nums) <= 100,000

BEFORE YOU CODE
  The brute force sums every window from scratch. What's its Big-O with k = 50,000?
  Which index LEAVES when nums[right] enters? (M5)
"""
from typing import List

# PLAN
# RETURNS:
# First window:
# Each slide (enters / leaves):
# Big-O:


def find_max_average(nums: List[int], k: int) -> float:
    pass


# ---------- tests: don't edit below ----------
import random
from _check import check

ENTRY = "find_max_average"


def _close(got, expected):
    return isinstance(got, (int, float)) and abs(got - expected) < 1e-5


CASES = [
    (([1, 12, -5, -6, 50, 3], 4), 12.75, "example"),
    (([5], 1), 5.0, "one item"),
    (([-1, -2, -3], 2), -1.5, "all negative"),
    (([4, 0, 4, 3, 3], 5), 2.8, "k = whole list"),
    (([0, 1, 1, 3, 3], 4), 2.0, "best at the end"),
    (([7, 7, 1, 1, 1], 2), 7.0, "best at the start"),
]
_r = random.Random(31)
PERF = [("100,000 items, k = 50,000", lambda: ([_r.randint(-10_000, 10_000) for _ in range(100_000)], 50_000), 1.0)]


def run_tests(fn):
    return check(fn, CASES, compare=_close, perf=PERF)


if __name__ == "__main__":
    run_tests(find_max_average)
