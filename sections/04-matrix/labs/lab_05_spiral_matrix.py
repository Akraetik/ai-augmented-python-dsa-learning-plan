"""
LAB 4.05 — Spiral Matrix                                     Tier: Build
LeetCode 54 (Medium) — https://leetcode.com/problems/spiral-matrix/
Lesson 4.3 · Pattern: four walls that shrink; re-check before the bottom row and the left column

THE PROBLEM (in our words)
Return every value of matrix (m × n) in spiral order: across the top, down the right side,
back across the bottom, up the left side, then the next ring inward.

RETURNS: List[int]

EXAMPLES
  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]          ->  [1, 2, 3, 6, 9, 8, 7, 4, 5]
  [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]  ->  [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

BEFORE YOU CODE
  Test [[1, 2, 3]] and [[1], [2], [3]] by hand FIRST. Which steps need a re-check, and why?
"""
from typing import List

# PLAN
# RETURNS:
# My four walls:
# The four steps, and which wall moves after each:
# The re-checks:


def spiral_order(matrix: List[List[int]]) -> List[int]:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "spiral_order"
CASES = [
    (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), [1, 2, 3, 6, 9, 8, 7, 4, 5], "3 x 3"),
    (([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], "3 x 4"),
    (([[1, 2, 3]],), [1, 2, 3], "one row"),
    (([[1], [2], [3]],), [1, 2, 3], "one column"),
    (([[7]],), [7], "one cell"),
    (([[1, 2], [3, 4], [5, 6]],), [1, 2, 4, 6, 5, 3], "tall"),
    (([[1, 2, 3, 4], [5, 6, 7, 8]],), [1, 2, 3, 4, 8, 7, 6, 5], "wide, two rows"),
]
PERF = [("500 x 500", lambda: ([[r * 500 + c for c in range(500)] for r in range(500)],), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(spiral_order)
