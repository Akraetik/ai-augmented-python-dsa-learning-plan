"""
LAB 4.07 — Set Matrix Zeroes                                 Tier: Build
LeetCode 73 (Medium) — https://leetcode.com/problems/set-matrix-zeroes/
Lesson 4.4 · Pattern: record first, write second; stretch goal: record in row 0 and column 0

THE PROBLEM (in our words)
If a cell is 0, set its entire row and entire column to 0. Do it in place.
This lab FAILS a full copy of the grid. It also reports whether you hit the O(1)-space follow-up.

RETURNS: None. Change matrix in place.

EXAMPLES
  [[1, 1, 1], [1, 0, 1], [1, 1, 1]]           ->  [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
  [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]  ->  [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

BEFORE YOU CODE
  Why does zeroing as soon as you see a 0 go wrong? Trace example 1.
  Version 1: two sets. Version 2: row 0 / column 0 as flags. Write the four steps for version 2.
"""
from typing import List

# PLAN
# RETURNS:
# Why not zero immediately:
# Version 1:
# Version 2 (four steps):


def set_zeroes(matrix: List[List[int]]) -> None:
    pass


# ---------- tests: don't edit below ----------
import tracemalloc
from _check import check

ENTRY = "set_zeroes"
CASES = [
    (([[1, 1, 1], [1, 0, 1], [1, 1, 1]],), [[1, 0, 1], [0, 0, 0], [1, 0, 1]], "example"),
    (([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],), [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]], "zeros in row 0"),
    (([[1, 2], [3, 4]],), [[1, 2], [3, 4]], "no zeros"),
    (([[0]],), [[0]], "one zero"),
    (([[1, 0]],), [[0, 0]], "one row"),
    (([[1], [0], [1]],), [[0], [0], [0]], "one column"),
    (([[1, 2, 3], [4, 5, 6], [7, 8, 0]],), [[1, 2, 0], [4, 5, 0], [0, 0, 0]], "zero in the corner"),
    (([[1, 1, 1], [0, 1, 1], [1, 1, 1]],), [[0, 1, 1], [0, 0, 0], [0, 1, 1]], "zero in column 0 only"),
    (([[1, 0, 1], [1, 1, 1], [1, 1, 1]],), [[0, 0, 0], [1, 0, 1], [1, 0, 1]], "zero in row 0 only"),
]


def _big():
    g = [[1] * 500 for _ in range(500)]
    for i in range(0, 500, 7):
        g[i][(i * 3) % 500] = 0
    return (g,)


PERF = [("500 x 500", _big, 1.5)]


def _memory(fn):
    grid = [[1] * 500 for _ in range(500)]
    for i in range(500):
        grid[i][(i * 7 + 3) % 500] = 0
    tracemalloc.start()
    fn(grid)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    no_copy = peak < 200_000
    o1 = peak < 4_000
    print(("PASS" if no_copy else "FAIL") + f" extra memory: {peak / 1000:.1f} KB (limit 200 KB — no full copy)")
    print(("BONUS" if o1 else "INFO") + (" O(1) follow-up reached: you stored the flags inside the grid."
                                          if o1 else " O(1) follow-up not reached yet. Try row 0 / column 0 as flags."))
    return no_copy


def run_tests(fn):
    ok = check(fn, CASES, inplace=0, perf=PERF)
    return _memory(fn) and ok if ok else False


if __name__ == "__main__":
    run_tests(set_zeroes)
