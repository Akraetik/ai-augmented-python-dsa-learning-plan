"""
LAB 4.01 — Transpose Matrix                                  Tier: Core
LeetCode 867 (Easy) — https://leetcode.com/problems/transpose-matrix/
(Extra rep: not on the Top 150. Grid indexing warm-up.)
Lesson 4.1 · Pattern: build a new grid of the new shape; out[c][r] = grid[r][c]

THE PROBLEM (in our words)
Return the transpose of matrix: row r, column c moves to row c, column r. The grid may not be square.

RETURNS: List[List[int]] — a NEW grid of shape cols × rows

EXAMPLES
  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]   ->  [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
  [[1, 2, 3], [4, 5, 6]]              ->  [[1, 4], [2, 5], [3, 6]]

DO IT TWICE
  1. With two loops. Build the output with a comprehension (not [[0] * x] * y — why?).
  2. With zip(*matrix). Explain what the * does.
"""
from typing import List

# PLAN
# RETURNS:
# Output shape:
# The copy rule:


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "transpose"
CASES = [
    (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), [[1, 4, 7], [2, 5, 8], [3, 6, 9]], "square"),
    (([[1, 2, 3], [4, 5, 6]],), [[1, 4], [2, 5], [3, 6]], "2 x 3"),
    (([[1], [2], [3]],), [[1, 2, 3]], "one column"),
    (([[7]],), [[7]], "one cell"),
    (([[1, 2]],), [[1], [2]], "one row"),
]
PERF = [("1,000 x 1,000", lambda: ([[r * 1000 + c for c in range(1000)] for r in range(1000)],), 2.0)]


def run_tests(fn):
    return check(fn, CASES, compare=lambda g, e: isinstance(g, list) and [list(x) for x in g] == e, perf=PERF)


if __name__ == "__main__":
    run_tests(transpose)
