"""
LAB 1.14 — Trapping Rain Water                               Tier: Stretch
LeetCode 42 (Hard) — https://leetcode.com/problems/trapping-rain-water/
Lesson 1.6 · Pattern: water[i] = min(max_left, max_right) - height[i]

THE PROBLEM (in our words)
height[i] is the height of a bar of width 1. After rain, how many units of water sit between the bars?

RETURNS: int

EXAMPLES
  [2, 0, 3, 1, 4, 2]                       ->  4
  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]     ->  6
  [4, 2, 0, 3, 2, 5]                       ->  9

CONSTRAINTS
  1 <= len(height) <= 20,000 (perf test: 100,000)
  0 <= height[i] <= 100,000

BEFORE YOU CODE
  Pick index 1 in the first example. What's the tallest bar to its left? To its right? How much water sits there?
  Do that for every index on paper. Then write the two sweeps.
  Later (Section 02): solve it again with two pointers and O(1) space.
"""
from typing import List

# PLAN
# RETURNS:
# Water at one index =
# The two lists I precompute:
# Idea + Big-O:


def trap(height: List[int]) -> int:
    pass


# ---------- tests: don't edit below ----------
import random
from _check import check

ENTRY = "trap"
CASES = [
    (([2, 0, 3, 1, 4, 2],), 4, "lesson picture"),
    (([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],), 6, "classic"),
    (([4, 2, 0, 3, 2, 5],), 9, "deep middle"),
    (([5],), 0, "one bar"),
    (([1, 2, 3, 4],), 0, "staircase up"),
    (([3, 0, 3],), 3, "one pit"),
    (([0, 0, 0],), 0, "flat ground"),
]
_r = random.Random(14)
PERF = [("100,000 bars", lambda: ([_r.randint(0, 100_000) for _ in range(100_000)],), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(trap)
