"""
LAB 0.10 — Speed Trap                                        Tier: Core
Pattern: find the hidden loop, remove it
Lesson: 00.2 (the "Hidden loops in Python" table)

THE PROBLEM
count_common(a, b) returns how many items in b also appear somewhere in a.
(Count every item of b, including repeats in b.)

The version below is CORRECT. Run this file now and watch it pass the small tests,
then get flagged SLOW on the big one. Your job: make it fast without changing what it returns.

RETURNS: int

EXAMPLES
  a = [1, 2, 3], b = [2, 2, 9]   ->  2    (both 2s count; 9 doesn't)

CONSTRAINTS
  0 <= len(a), len(b) <= 100,000

THINK ABOUT
  The code has one visible loop. Why is it O(n^2) anyway?
  Write the real Big-O of the slow version in your PLAN before you change anything.
"""
from typing import List

# PLAN
# Real Big-O of the slow version, and why:
# Fix:
# New Big-O (time and space):


def count_common(a: List[int], b: List[int]) -> int:
    count = 0
    for x in b:
        if x in a:
            count += 1
    return count


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "count_common"
CASES = [
    (([1, 2, 3], [2, 2, 9]), 2, "example"),
    (([], [1, 2]), 0, "a empty"),
    (([1, 2], []), 0, "b empty"),
    (([5, 5, 5], [5]), 1, "repeats in a"),
    (([-1, 0], [0, -1, 1]), 2, "negatives"),
]
PERF = [("100,000 x 100,000", lambda: (list(range(100_000)), list(range(50_000, 150_000))), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(count_common)
