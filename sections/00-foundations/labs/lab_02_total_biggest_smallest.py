"""
LAB 0.02 — Total, Biggest, Smallest                          Tier: Warm-up
Pattern: one pass, keep running values
Lesson: 00.3

THE PROBLEM
Given a non-empty list of integers, return three things as a tuple:
(the total, the biggest value, the smallest value).

RULE: don't use sum(), max(), or min(). Build them yourself with one loop.
This is the "running value" pattern. You'll use it in half the problems in Section 1.

RETURNS: a tuple (total, biggest, smallest)

EXAMPLES
  [4, -2, 9]   ->  (11, 9, -2)
  [5]          ->  (5, 5, 5)

CONSTRAINTS
  1 <= len(nums) <= 100,000
  -1,000,000 <= nums[i] <= 1,000,000

THINK ABOUT
  What should "biggest" start as, before you've seen anything? Two good options exist.
"""
from typing import List, Tuple

# PLAN (fill in before coding)
# RETURNS:
# Restate:
# Example by hand:
# Edge cases:
# Idea + Big-O:


def stats(nums: List[int]) -> Tuple[int, int, int]:
    pass


# ---------- tests: don't edit below ----------
import random
from _check import check

ENTRY = "stats"
CASES = [
    (([4, -2, 9],), (11, 9, -2), "example"),
    (([5],), (5, 5, 5), "one item"),
    (([-3, -1, -7],), (-11, -1, -7), "all negative"),
    (([2, 2, 2, 2],), (8, 2, 2), "all same"),
    (([0, 1000000, -1000000],), (0, 1000000, -1000000), "extremes"),
]
_r = random.Random(1)
PERF = [("100,000 numbers", lambda: ([_r.randint(-10**6, 10**6) for _ in range(100_000)],), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(stats)
