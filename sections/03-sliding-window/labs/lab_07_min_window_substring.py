"""
LAB 3.07 — Minimum Window Substring                          Tier: Stretch
LeetCode 76 (Hard) — https://leetcode.com/problems/minimum-window-substring/
Lesson 3.3 · Pattern: shortest valid window with need/have counts

THE PROBLEM (in our words)
Return the shortest substring of s that contains every character of t, including repeats
(if t has two 'a's, the window needs at least two). If none exists, return "".
The answer is unique when it exists.

RETURNS: str (the substring itself)

EXAMPLES
  s = "ADOBECODEBANC", t = "ABC"   ->  "BANC"
  s = "a", t = "a"                 ->  "a"
  s = "a", t = "aa"                ->  ""

CONSTRAINTS
  1 <= len(s), len(t) <= 100,000 (perf test: s = 100,000, t = 50)

BEFORE YOU CODE
  Trace s = "XAYBZACB", t = "ABC" by hand (answer "ACB").
  What do `need`, `have`, and `required` mean? When exactly does `have` go up? Down?
  You return a substring, so what must you record besides the length?
"""

# PLAN
# RETURNS:
# need / required:
# have goes up when ___, down when ___:
# What I record:


def min_window(s: str, t: str) -> str:
    pass


# ---------- tests: don't edit below ----------
import random
import string
from _check import check

ENTRY = "min_window"
CASES = [
    (("ADOBECODEBANC", "ABC"), "BANC", "example"),
    (("a", "a"), "a", "single"),
    (("a", "aa"), "", "needs two, only one"),
    (("XAYBZACB", "ABC"), "ACB", "lesson trace"),
    (("aa", "aa"), "aa", "repeats in t"),
    (("ab", "b"), "b", "one letter at the end"),
    (("bba", "ab"), "ba", "shrink past extra copies"),
    (("abc", "d"), "", "letter missing"),
]


def _big():
    r = random.Random(37)
    t = "".join(r.choice(string.ascii_uppercase) for _ in range(50))
    s = "".join(r.choice(string.ascii_lowercase) for _ in range(99_000)) + t[::-1] + "x" * 950
    return (s, t)


PERF = [("s = 100,000, t = 50", _big, 1.5)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(min_window)
