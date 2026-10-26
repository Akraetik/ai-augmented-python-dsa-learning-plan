"""
LAB 2.01 — Valid Palindrome                                  Tier: Core
LeetCode 125 (Easy) — https://leetcode.com/problems/valid-palindrome/
Lesson 2.1 · Pattern: opposite ends, skip what doesn't count

THE PROBLEM (in our words)
Ignore every character that isn't a letter or a digit, and ignore upper/lower case.
Does what's left read the same forward and backward?

RETURNS: bool

EXAMPLES
  "A man, a plan, a canal: Panama"   ->  True
  "race a car"                       ->  False
  " "                                ->  True    (nothing left counts as a palindrome)

CONSTRAINTS
  1 <= len(s) <= 200,000

DO IT TWICE
  1. Build a cleaned list, compare it with its reverse. O(n) space.
  2. Two pointers on s itself, skipping junk in place. O(1) space.
     Your skip loops need `left < right` too. Why? Try ".,!".
"""

# PLAN
# RETURNS:
# What I compare:
# How I skip junk (and the guard):
# Idea + Big-O:


def is_palindrome(s: str) -> bool:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "is_palindrome"
CASES = [
    (("A man, a plan, a canal: Panama",), True, "example"),
    (("race a car",), False, "not a palindrome"),
    ((" ",), True, "only a space"),
    (("0P",), False, "digit vs letter"),
    (("ab_a",), True, "underscore is junk"),
    ((".,!",), True, "all junk"),
    (("No 'x' in Nixon",), True, "mixed case and quotes"),
    (("a",), True, "one char"),
    (("12321",), True, "digits"),
]
PERF = [("200,000 chars", lambda: ("Ab, " * 25_000 + " ,bA" * 25_000,), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(is_palindrome)
