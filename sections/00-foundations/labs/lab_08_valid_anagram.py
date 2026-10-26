"""
LAB 0.08 — Valid Anagram                                     Tier: Core
LeetCode 242 (Easy) — https://leetcode.com/problems/valid-anagram/
Pattern: counting (dict / Counter), or sort-and-compare
Lesson: 00.4

THE PROBLEM (in our words)
Two strings are anagrams if they use exactly the same letters the same number of times,
just in a different order. Return True if s and t are anagrams.

RETURNS: bool

EXAMPLES
  "listen", "silent"   ->  True
  "rat", "car"         ->  False
  "aab", "abb"         ->  False   (same letters, different counts)

CONSTRAINTS
  1 <= len(s), len(t) <= 50,000
  lowercase English letters only

CHALLENGE
  Solve it two ways. Way 1: sorting. Way 2: counting. Write the Big-O of each in your PLAN.
  Which one is faster in Big-O terms? Which one is shorter to write?
"""

# PLAN
# RETURNS:
# Quick reject check (one line):
# Way 1 + Big-O:
# Way 2 + Big-O:


def is_anagram(s: str, t: str) -> bool:
    pass


# ---------- tests: don't edit below ----------
import random
import string
from _check import check

ENTRY = "is_anagram"
CASES = [
    (("listen", "silent"), True, "example"),
    (("rat", "car"), False, "different letters"),
    (("aab", "abb"), False, "different counts"),
    (("a", "a"), True, "one letter"),
    (("ab", "abc"), False, "different lengths"),
    (("anagram", "nagaram"), True, "repeats"),
]
_r = random.Random(8)
_s = "".join(_r.choice(string.ascii_lowercase) for _ in range(50_000))
PERF = [("50,000 chars", lambda: (_s, "".join(sorted(_s))), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(is_anagram)
