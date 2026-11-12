"""
LAB 4.04 — Rotate Image                                      Tier: Build
LeetCode 48 (Medium) — https://leetcode.com/problems/rotate-image/
Lesson 4.3 · Pattern: transpose in place, then reverse each row

THE PROBLEM (in our words)
matrix is n × n. Rotate it 90 degrees clockwise, IN PLACE. Don't build a second grid.
This lab measures extra memory on a 1,000 × 1,000 grid.

RETURNS: None. Change matrix in place. (M6)

EXAMPLES
  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]   ->  [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
  [[1, 2], [3, 4]]                    ->  [[3, 1], [4, 2]]

BEFORE YOU CODE
  In-place transpose: which cells do you swap? What goes wrong if you swap every (r, c) with (c, r)?
"""
from typing import List

# PLAN
# RETURNS:
# Step 1 (and which cells I loop over):
# Step 2:


def rotate(matrix: List[List[int]]) -> None:
    pass


# ---------- tests: don't edit below ----------
import tracemalloc
from _check import check

ENTRY = "rotate"
CASES = [
    (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), [[7, 4, 1], [8, 5, 2], [9, 6, 3]], "3 x 3"),
    (([[1, 2], [3, 4]],), [[3, 1], [4, 2]], "2 x 2"),
    (([[5]],), [[5]], "1 x 1"),
    (([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],),
     [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]], "4 x 4"),
]
_N = 1_000
PERF = [("1,000 x 1,000", lambda: ([[r * _N + c for c in range(_N)] for r in range(_N)],), 2.0)]


def _memory_ok(fn):
    grid = [[r * _N + c for c in range(_N)] for r in range(_N)]
    tracemalloc.start()
    fn(grid)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    ok = peak < 200_000
    print(("PASS" if ok else "FAIL") + f" extra memory: {peak / 1000:.0f} KB (limit 200 KB)"
          + ("" if ok else " — that's a second grid. Rotate in place: transpose, then reverse each row."))
    return ok


def run_tests(fn):
    ok = check(fn, CASES, inplace=0, perf=PERF)
    return _memory_ok(fn) and ok if ok else False


if __name__ == "__main__":
    run_tests(rotate)
