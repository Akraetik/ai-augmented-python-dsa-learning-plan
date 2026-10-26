"""
LAB 1.20 — Find the Index of the First Occurrence in a String   Tier: Core
LeetCode 28 (Easy) — https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Lesson 1.8 · Pattern: try each start, compare, stop at the first mismatch

THE PROBLEM (in our words)
Return the index where needle first appears inside haystack, or -1 if it never does.

RULE: don't use .find(), .index(), or `in`. Compare characters yourself (you may use slicing to compare
one window, but think about what that slice costs).

RETURNS: int

EXAMPLES
  haystack = "sadbutsad", needle = "sad"    ->  0
  haystack = "leetcode", needle = "leeto"   ->  -1
  haystack = "hello", needle = "ll"         ->  2

CONSTRAINTS
  1 <= len(haystack), len(needle) <= 10,000

BEFORE YOU CODE
  haystack length 9, needle length 3: what's the LAST start index worth trying? Write the general formula. (M5)
"""

# PLAN
# RETURNS:
# Last start index:
# Idea + Big-O:


def str_str(haystack: str, needle: str) -> int:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "str_str"
CASES = [
    (("sadbutsad", "sad"), 0, "example"),
    (("leetcode", "leeto"), -1, "not found"),
    (("hello", "ll"), 2, "middle"),
    (("abc", "c"), 2, "at the very end"),
    (("a", "a"), 0, "same string"),
    (("ab", "abc"), -1, "needle longer"),
    (("mississippi", "issip"), 4, "false start first"),
]
PERF = [("10,000 vs 100", lambda: ("a" * 9_900 + "b" * 100, "b" * 100), 2.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(str_str)
