"""
LAB 3.02 — Permutation in String                             Tier: Build
LeetCode 567 (Medium) — https://leetcode.com/problems/permutation-in-string/
(Extra rep from NeetCode 150. Fixed window of COUNTS.)
Lesson 3.1 · Pattern: fixed window of letter counts, compare to the target counts

THE PROBLEM (in our words)
Return True if s2 contains some rearrangement of s1 as a block of letters next to each other.

RETURNS: bool

EXAMPLES
  s1 = "ab", s2 = "eidbaooo"   ->  True    ("ba")
  s1 = "ab", s2 = "eidboaoo"   ->  False
  s1 = "abc", s2 = "ab"        ->  False   (s1 is longer)

CONSTRAINTS
  1 <= len(s1), len(s2) <= 10,000 (perf test: s2 = 100,000), lowercase letters

BEFORE YOU CODE
  What does "is a rearrangement of" mean in terms of counts?
  How big is the window? What changes in the counts when it slides one step?
"""

# PLAN
# RETURNS:
# Window size:
# What I compare each step:
# Big-O:


def check_inclusion(s1: str, s2: str) -> bool:
    pass


# ---------- tests: don't edit below ----------
import random
import string
from _check import check

ENTRY = "check_inclusion"
CASES = [
    (("ab", "eidbaooo"), True, "example"),
    (("ab", "eidboaoo"), False, "letters not adjacent"),
    (("abc", "ab"), False, "s1 longer"),
    (("a", "a"), True, "same single letter"),
    (("adc", "dcda"), True, "at the very end"),
    (("aab", "abbab"), False, "counts matter"),
    (("hello", "ooolleoooleh"), False, "close but no"),
    (("abc", "bbbca"), True, "overlapping repeats"),
]


def _big():
    r = random.Random(32)
    s1 = "".join(r.choice(string.ascii_lowercase) for _ in range(5_000))
    s2 = "".join(r.choice(string.ascii_lowercase) for _ in range(95_000))
    return (s1, s2 + "".join(sorted(s1)))      # the only match is at the very end


PERF = [("s1 = 5,000, s2 = 100,000", _big, 1.5)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(check_inclusion)
