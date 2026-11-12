"""
LAB 4.03 — Valid Sudoku                                      Tier: Build
LeetCode 36 (Medium) — https://leetcode.com/problems/valid-sudoku/
Lesson 4.2 · Pattern: one set per row, column, and box; box = (r // 3) * 3 + c // 3

THE PROBLEM (in our words)
board is 9 × 9. Each cell is "1"-"9" or "." (empty). Return True if no digit repeats in any row,
any column, or any 3 × 3 box. You don't solve the puzzle. You only check what's filled in.

RETURNS: bool

BEFORE YOU CODE
  Write the box formula and check it on cell (4, 7) → box 5.
  When can you return True? (M7)
"""
from typing import List

# PLAN
# RETURNS:
# My sets:
# Box formula:
# Return True when:


def is_valid_sudoku(board: List[List[str]]) -> bool:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "is_valid_sudoku"
_GOOD = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


def _with(r, c, d):
    b = [row[:] for row in _GOOD]
    b[r][c] = d
    return b


_EMPTY = [["."] * 9 for _ in range(9)]
_BOX_ONLY = [row[:] for row in _EMPTY]
_BOX_ONLY[3][3] = "4"
_BOX_ONLY[5][5] = "4"       # same box 4, different row and column
_LAST = [row[:] for row in _EMPTY]
_LAST[8][0] = "9"
_LAST[8][8] = "9"           # repeat in the last row

CASES = [
    ((_GOOD,), True, "valid board"),
    ((_with(0, 0, "8"),), False, "column repeat (8 in column 0)"),
    ((_with(0, 2, "5"),), False, "row repeat (5 in row 0)"),
    ((_BOX_ONLY,), False, "box repeat only"),
    ((_EMPTY,), True, "empty board"),
    ((_LAST,), False, "repeat in the last row"),
    ((_with(1, 1, "8"),), False, "box 0 repeat (8)"),
]
PERF = []


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(is_valid_sudoku)
