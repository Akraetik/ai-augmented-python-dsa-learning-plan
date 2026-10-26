"""
LAB 1.19 — Reverse Words in a String                         Tier: Build
LeetCode 151 (Medium) — https://leetcode.com/problems/reverse-words-in-a-string/
Lesson 1.8 · Pattern: split, reverse, join (and the two-reversal trick)
You've seen this one before. Solve it fresh, then try the no-split version.

THE PROBLEM (in our words)
Return the words of s in reverse order, separated by single spaces.
No leading or trailing spaces in the answer, even if s has them. Multiple spaces between words become one.

RETURNS: str

EXAMPLES
  "the sky is blue"       ->  "blue is sky the"
  "  hello world  "       ->  "world hello"
  "a good   example"      ->  "example good a"

CONSTRAINTS
  1 <= len(s) <= 10,000 (perf test: 100,000), at least one word

DO IT TWICE
  1. split / reverse / join. Explain why it already handles every spacing case.
  2. No split(): walk the string, collect words by hand. Then join.
"""

# PLAN
# RETURNS:
# Way 1 + why spaces are handled:
# Way 2 steps:


def reverse_words(s: str) -> str:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "reverse_words"
CASES = [
    (("the sky is blue",), "blue is sky the", "example"),
    (("  hello world  ",), "world hello", "outer spaces"),
    (("a good   example",), "example good a", "inner spaces"),
    (("one",), "one", "one word"),
    (("   spaced   ",), "spaced", "one word, spaces"),
]
PERF = [("100,000 chars", lambda: ("ab  " * 25_000,), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(reverse_words)
