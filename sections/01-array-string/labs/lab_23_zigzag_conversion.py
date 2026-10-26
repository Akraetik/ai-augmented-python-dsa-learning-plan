"""
LAB 1.23 — Zigzag Conversion                                 Tier: Build
LeetCode 6 (Medium) — https://leetcode.com/problems/zigzag-conversion/
Lesson 1.8 · Pattern: simulate with a direction flag

THE PROBLEM (in our words)
Write s down a zigzag over num_rows rows (down, then diagonally up, then down again...).
Then read the rows left to right, top row first, and return that string.

  num_rows = 3, s = "PAYPALISHIRING"
  P   A   H   N
  A P L S I I G
  Y   I   R
  -> "PAHNAPLSIIGYIR"

RETURNS: str

EXAMPLES
  "PAYPALISHIRING", 3   ->  "PAHNAPLSIIGYIR"
  "PAYPALISHIRING", 4   ->  "PINALSIGYAHRPI"
  "A", 1                ->  "A"

CONSTRAINTS
  1 <= len(s) <= 1,000 (perf test: 100,000), 1 <= num_rows <= 1,000

BEFORE YOU CODE
  Don't look for a formula. Simulate: one list per row, a current row, and a step of +1 or -1.
  When does the step flip? What breaks when num_rows == 1? Test it.
"""

# PLAN
# RETURNS:
# State I keep:
# When the direction flips:
# Special case:


def convert(s: str, num_rows: int) -> str:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "convert"
CASES = [
    (("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR", "3 rows"),
    (("PAYPALISHIRING", 4), "PINALSIGYAHRPI", "4 rows"),
    (("A", 1), "A", "one char"),
    (("ABCDE", 1), "ABCDE", "one row"),
    (("ABCDE", 2), "ACEBD", "two rows"),
    (("AB", 5), "AB", "more rows than chars"),
]
PERF = [("100,000 chars, 7 rows", lambda: ("abcdefghij" * 10_000, 7), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(convert)
