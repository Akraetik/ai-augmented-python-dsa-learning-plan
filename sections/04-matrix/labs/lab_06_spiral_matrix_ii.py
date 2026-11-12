"""
LAB 4.06 — Spiral Matrix II                                  Tier: Build
LeetCode 59 (Medium) — https://leetcode.com/problems/spiral-matrix-ii/
(Extra rep: not on the Top 150. The same walk, writing instead of reading.)
Lesson 4.3 · Pattern: four walls, or one direction at a time with (d + 1) % 4 turns

THE PROBLEM (in our words)
Build an n × n grid filled with 1, 2, ..., n² in spiral order.

RETURNS: List[List[int]]

EXAMPLES
  3   ->  [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
  1   ->  [[1]]

BEFORE YOU CODE
  Build the empty grid safely (Section 00 trap). Then: four walls, or the turning walker?
  Try the method you did NOT use in lab 05.
"""
from typing import List

# PLAN
# RETURNS:
# Empty grid:
# Walk method:


def generate_matrix(n: int) -> List[List[int]]:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "generate_matrix"
CASES = [
    ((3,), [[1, 2, 3], [8, 9, 4], [7, 6, 5]], "n = 3"),
    ((1,), [[1]], "n = 1"),
    ((2,), [[1, 2], [4, 3]], "n = 2"),
    ((4,), [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]], "n = 4"),
]
PERF = [("n = 500", lambda: (500,), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(generate_matrix)
