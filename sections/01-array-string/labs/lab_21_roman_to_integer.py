"""
LAB 1.21 — Roman to Integer                                  Tier: Core
LeetCode 13 (Easy) — https://leetcode.com/problems/roman-to-integer/
Lesson 1.8 · Pattern: lookup table + peek at the next symbol

THE PROBLEM (in our words)
Convert a Roman numeral to an integer.
  I=1  V=5  X=10  L=50  C=100  D=500  M=1000
Symbols usually go biggest to smallest and add up. Six special pairs subtract:
  IV=4  IX=9  XL=40  XC=90  CD=400  CM=900

RETURNS: int

EXAMPLES
  "III"      ->  3
  "LVIII"    ->  58
  "MCMXCIV"  ->  1994

CONSTRAINTS
  valid numerals for 1..3999

BEFORE YOU CODE
  State the subtract rule in ONE sentence using "the next symbol."
  What happens at the last symbol, where there is no next? (M5)
"""

# PLAN
# RETURNS:
# Subtract rule:
# Last symbol:
# Idea + Big-O:


def roman_to_int(s: str) -> int:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "roman_to_int"
CASES = [
    (("III",), 3, "example"),
    (("LVIII",), 58, "adding only"),
    (("MCMXCIV",), 1994, "three subtract pairs"),
    (("IV",), 4, "IV"),
    (("IX",), 9, "IX"),
    (("XL",), 40, "XL"),
    (("CD",), 400, "CD"),
    (("MMMCMXCIX",), 3999, "biggest"),
    (("I",), 1, "smallest"),
]
PERF = []


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(roman_to_int)
