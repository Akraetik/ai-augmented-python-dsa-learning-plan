"""
LAB 2.06 — 3Sum                                              Tier: Build
LeetCode 15 (Medium) — https://leetcode.com/problems/3sum/
Lesson 2.4 · Pattern: sort, fix one, two-pointer the rest, skip duplicates

THE PROBLEM (in our words)
Return every UNIQUE triple of values [a, b, c] from nums (three different positions) with a + b + c == 0.
No duplicate triples. Order of triples, and order inside a triple, don't matter.

RETURNS: List[List[int]]

EXAMPLES
  [-1, 0, 1, 2, -1, -4]   ->  [[-1, -1, 2], [-1, 0, 1]]
  [0, 1, 1]               ->  []
  [0, 0, 0]               ->  [[0, 0, 0]]

CONSTRAINTS
  3 <= len(nums) <= 3,000

BEFORE YOU CODE
  List the THREE places you skip duplicates (lesson 2.4). Trace [-2, 0, 0, 2, 2].
  Why `nums[i] == nums[i - 1]` and not `nums[i] == nums[i + 1]`? Trace [-1, -1, 2].
"""
from typing import List

# PLAN
# RETURNS:
# After sorting, for each i:
# Duplicate skip 1:
# Duplicate skip 2 and 3:
# Big-O:


def three_sum(nums: List[int]) -> List[List[int]]:
    pass


# ---------- tests: don't edit below ----------
import random
from _check import check

ENTRY = "three_sum"


def _same(got, expected):
    if not isinstance(got, list):
        return False
    try:
        g = sorted(tuple(sorted(t)) for t in got)
    except TypeError:
        return False
    return g == sorted(tuple(sorted(t)) for t in expected)


CASES = [
    (([-1, 0, 1, 2, -1, -4],), [[-1, -1, 2], [-1, 0, 1]], "example"),
    (([0, 1, 1],), [], "none"),
    (([0, 0, 0],), [[0, 0, 0]], "all zeros"),
    (([0, 0, 0, 0],), [[0, 0, 0]], "four zeros, one triple"),
    (([-2, 0, 1, 1, 2],), [[-2, 0, 2], [-2, 1, 1]], "two triples"),
    (([-2, 0, 0, 2, 2],), [[-2, 0, 2]], "duplicates after a match"),
    (([-1, -1, 2],), [[-1, -1, 2]], "first copy must pair with the second"),
    (([3, -2, 1, 0],), [], "no zero sum"),
]


def _big():
    r = random.Random(15)
    return ([r.randint(-100_000, 100_000) for _ in range(3_000)],)


PERF = [("3,000 numbers", _big, 3.0)]


def run_tests(fn):
    return check(fn, CASES, compare=_same, perf=PERF)


if __name__ == "__main__":
    run_tests(three_sum)
