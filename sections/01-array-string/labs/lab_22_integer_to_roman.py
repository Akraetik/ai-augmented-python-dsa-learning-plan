"""
LAB 1.22 — Integer to Roman                                  Tier: Build
LeetCode 12 (Medium) — https://leetcode.com/problems/integer-to-roman/
Lesson 1.8 · Pattern: greedy, biggest value first

THE PROBLEM (in our words)
Convert an integer from 1 to 3999 into a Roman numeral. Same symbols and special pairs as lab 21.

RETURNS: str

EXAMPLES
  3      ->  "III"
  58     ->  "LVIII"
  1994   ->  "MCMXCIV"

BEFORE YOU CODE
  Write the full list of (value, symbol) pairs, biggest first, INCLUDING the six special pairs.
  Why does including 900, 400, 90, 40, 9, 4 make greedy correct?
"""

# PLAN
# RETURNS:
# My value/symbol list:
# Idea + Big-O:


def int_to_roman(num: int) -> str:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "int_to_roman"
CASES = [
    ((3,), "III", "example"),
    ((58,), "LVIII", "example 2"),
    ((1994,), "MCMXCIV", "example 3"),
    ((4,), "IV", "4"),
    ((9,), "IX", "9"),
    ((40,), "XL", "40"),
    ((444,), "CDXLIV", "three subtract pairs"),
    ((3999,), "MMMCMXCIX", "biggest"),
    ((1,), "I", "smallest"),
]
PERF = []


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(int_to_roman)
