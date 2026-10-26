"""
LAB 2.05 — Container With Most Water                         Tier: Build
LeetCode 11 (Medium) — https://leetcode.com/problems/container-with-most-water/
Lesson 2.3 · Pattern: start wide, move the shorter side inward

THE PROBLEM (in our words)
height[i] is a vertical line at position i. Two lines and the floor make a container.
Return the most water any container can hold: (j - i) × min(height[i], height[j]).

RETURNS: int

EXAMPLES
  [1, 8, 6, 2, 5, 4, 8, 3, 7]   ->  49   (lines 1 and 8: width 7 × height 7)
  [1, 1]                        ->  1

CONSTRAINTS
  2 <= len(height) <= 100,000

BEFORE YOU CODE
  Write the one-sentence proof that moving the SHORTER line can't lose the answer.
  The perf test will fail the every-pair version. Check.
"""
from typing import List

# PLAN
# RETURNS:
# Area formula:
# Which pointer moves, and why it's safe:
# Idea + Big-O:


def max_area(height: List[int]) -> int:
    pass


# ---------- tests: don't edit below ----------
import random
from _check import check

ENTRY = "max_area"
CASES = [
    (([1, 8, 6, 2, 5, 4, 8, 3, 7],), 49, "example"),
    (([1, 1],), 1, "two lines"),
    (([4, 3, 2, 1, 4],), 16, "best is the widest"),
    (([1, 2, 1],), 2, "short ends"),
    (([2, 3, 4, 5, 18, 17, 6],), 17, "tall pair in the middle"),
    (([0, 0, 0],), 0, "flat"),
]
_r = random.Random(25)
PERF = [("100,000 lines", lambda: ([_r.randint(0, 10_000) for _ in range(100_000)],), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(max_area)
