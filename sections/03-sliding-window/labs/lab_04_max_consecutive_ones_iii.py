"""
LAB 3.04 — Max Consecutive Ones III                          Tier: Build
LeetCode 1004 (Medium) — https://leetcode.com/problems/max-consecutive-ones-iii/
(Extra rep from LeetCode 75. Section 00's lab 0.07 with a shrink step.)
Lesson 3.2 · Pattern: variable window, longest valid — at most k zeros inside

THE PROBLEM (in our words)
nums holds only 0s and 1s. You may flip at most k zeros to 1. Return the longest run of 1s you can get.

RETURNS: int

EXAMPLES
  nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2   ->  6
  nums = [0, 0, 1, 1], k = 0                        ->  2

CONSTRAINTS
  1 <= len(nums) <= 100,000,  0 <= k <= len(nums)

BEFORE YOU CODE
  Restate it as a window rule. You never flip anything. What do you count?
"""
from typing import List

# PLAN
# RETURNS:
# The window rule (restated):
# What I count, and when it changes:
# Big-O:


def longest_ones(nums: List[int], k: int) -> int:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "longest_ones"
CASES = [
    (([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6, "example"),
    (([0, 0, 1, 1], 0), 2, "k = 0"),
    (([0, 0, 0], 2), 2, "all zeros"),
    (([0, 0, 0], 3), 3, "flip them all"),
    (([1, 1, 1], 1), 3, "no zeros to flip"),
    (([1, 0, 1, 1, 0, 1], 1), 4, "two equal best windows"),
    (([0], 0), 0, "one zero, no flips"),
]
PERF = [("100,000 items, k = 5,000", lambda: ([1, 0] * 50_000, 5_000), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(longest_ones)
