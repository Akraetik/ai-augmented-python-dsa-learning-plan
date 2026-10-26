"""
LAB 2.08 — 3Sum Closest                                      Tier: Build
LeetCode 16 (Medium) — https://leetcode.com/problems/3sum-closest/
(Extra rep: not on the Top 150. Same shape as 3Sum, easier bookkeeping.)
Lesson 2.4 · Pattern: sort, fix one, two-pointer the rest, track the best

THE PROBLEM (in our words)
Pick three numbers at different positions. Return the SUM of the three whose sum is closest to target.
There is exactly one closest sum.

RETURNS: int (the sum, not the numbers — M6)

EXAMPLES
  [-1, 2, 1, -4], target 1   ->  2     (-1 + 2 + 1)
  [0, 0, 0], target 1        ->  0

CONSTRAINTS
  3 <= len(nums) <= 500 (perf test: 2,000)
"""
from typing import List

# PLAN
# RETURNS:
# What "best" tracks and how I compare:
# Pointer moves:
# Early exit:


def three_sum_closest(nums: List[int], target: int) -> int:
    pass


# ---------- tests: don't edit below ----------
import random
from _check import check

ENTRY = "three_sum_closest"
CASES = [
    (([-1, 2, 1, -4], 1), 2, "example"),
    (([0, 0, 0], 1), 0, "all zeros"),
    (([1, 1, 1, 0], -100), 2, "target far below"),
    (([4, 0, 5, -5, 3, 3, 0, -4, -5], -2), -2, "exact hit"),
    (([1, 2, 4, 8, 16, 32, 64, 128], 82), 82, "exact hit 2"),
    (([1, 1, -1, -1, 3], -1), -1, "negatives"),
]


def _big():
    r = random.Random(16)
    return ([r.randint(-10_000, 10_000) for _ in range(2_000)], 12_345)


PERF = [("2,000 numbers", _big, 2.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(three_sum_closest)
