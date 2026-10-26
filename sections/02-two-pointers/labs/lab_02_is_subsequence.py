"""
LAB 2.02 — Is Subsequence                                    Tier: Core
LeetCode 392 (Easy) — https://leetcode.com/problems/is-subsequence/
Lesson 2.2 · Pattern: same direction — one pointer per string, the slow one moves on a match

THE PROBLEM (in our words)
Return True if you can delete zero or more characters from t, without changing the order of the rest,
and end up with s.

RETURNS: bool

EXAMPLES
  s = "abc", t = "ahbgdc"   ->  True
  s = "axc", t = "ahbgdc"   ->  False
  s = "",    t = "abc"      ->  True

CONSTRAINTS
  0 <= len(s) <= 100,  0 <= len(t) <= 10,000   (perf test: much bigger)

BEFORE YOU CODE
  Which pointer moves every step? Which moves only on a match? When do you return True?
"""

# PLAN
# RETURNS:
# Fast pointer / slow pointer:
# Return True when:
# Edge cases:


def is_subsequence(s: str, t: str) -> bool:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "is_subsequence"
CASES = [
    (("abc", "ahbgdc"), True, "example"),
    (("axc", "ahbgdc"), False, "missing letter"),
    (("", "abc"), True, "empty s"),
    (("abc", ""), False, "empty t"),
    (("aec", "abcde"), False, "wrong order"),
    (("aaa", "aa"), False, "s longer than t"),
    (("ace", "abcde"), True, "skips"),
    (("b", "abc"), True, "single char"),
]
PERF = [("100,000 vs 1,000,000", lambda: ("ab" * 50_000, "aXbY" * 250_000), 1.5)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(is_subsequence)
