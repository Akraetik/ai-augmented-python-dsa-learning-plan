"""
LAB 3.05 — Longest Repeating Character Replacement           Tier: Build
LeetCode 424 (Medium) — https://leetcode.com/problems/longest-repeating-character-replacement/
(Extra rep from NeetCode 150.)
Lesson 3.2 · Pattern: variable window — changes needed = length − most common count

THE PROBLEM (in our words)
s is uppercase letters. You may change at most k letters to any other letter.
Return the length of the longest block you can make all the same letter.

RETURNS: int

EXAMPLES
  s = "ABAB", k = 2      ->  4
  s = "AABABBA", k = 1   ->  4   ("AABA" → "AAAA", or "ABBB" → "BBBB")

CONSTRAINTS
  1 <= len(s) <= 100,000,  0 <= k <= len(s)

BEFORE YOU CODE
  In a window, which letter do you keep, and how many changes does that cost?
  When is the window broken?
"""

# PLAN
# RETURNS:
# Changes needed in a window:
# Broken when:
# Big-O:


def character_replacement(s: str, k: int) -> int:
    pass


# ---------- tests: don't edit below ----------
import random
from _check import check

ENTRY = "character_replacement"
CASES = [
    (("ABAB", 2), 4, "example"),
    (("AABABBA", 1), 4, "example 2"),
    (("A", 0), 1, "one letter"),
    (("ABCDE", 0), 1, "no changes allowed"),
    (("ABCDE", 10), 5, "k bigger than s"),
    (("AAAB", 0), 3, "run at the start"),
    (("BAAAB", 2), 5, "change both ends"),
    (("ABBB", 2), 4, "most common is not the first letter"),
]
_r = random.Random(35)
PERF = [("100,000 letters, k = 1,000", lambda: ("".join(_r.choice("AB") for _ in range(100_000)), 1_000), 1.5)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(character_replacement)
