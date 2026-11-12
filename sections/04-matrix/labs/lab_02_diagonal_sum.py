"""
LAB 4.02 — Matrix Diagonal Sum                               Tier: Core
LeetCode 1572 (Easy) — https://leetcode.com/problems/matrix-diagonal-sum/
(Extra rep: not on the Top 150.)
Lesson 4.1 · Pattern: one loop over i gives both diagonals

THE PROBLEM (in our words)
mat is n × n. Return the sum of the main diagonal plus the anti-diagonal.
If n is odd, the center cell sits on both. Count it once.

RETURNS: int

EXAMPLES
  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]   ->  25   (1 + 5 + 9 + 3 + 7)
  [[1, 1], [1, 1]]                    ->  4
  [[5]]                               ->  5

CONSTRAINTS
  1 <= n <= 100 on LeetCode. The perf test uses n = 6,000: scanning every cell is too slow.

BEFORE YOU CODE
  Which cells are on each diagonal? Write them in terms of i and n.
"""
from typing import List

# PLAN
# RETURNS:
# Main diagonal cells:
# Anti-diagonal cells:
# Odd n:


def diagonal_sum(mat: List[List[int]]) -> int:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "diagonal_sum"
CASES = [
    (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), 25, "odd n, shared center"),
    (([[1, 1], [1, 1]],), 4, "even n"),
    (([[5]],), 5, "one cell"),
    (([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],), 8, "4 x 4"),
    (([[7, 3, 1, 9], [3, 4, 6, 9], [6, 9, 6, 6], [9, 5, 8, 5]],), 55, "mixed values"),
]


def _big():
    row = list(range(6_000))
    return ([row] * 6_000,)       # every row is the same list: fine, we only read


PERF = [("6,000 x 6,000", _big, 0.25)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(diagonal_sum)
