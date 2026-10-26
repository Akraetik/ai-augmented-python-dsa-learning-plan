"""
LAB 1.15 — Candy                                             Tier: Stretch
LeetCode 135 (Hard) — https://leetcode.com/problems/candy/
Lesson 1.6 · Pattern: one sweep per neighbor rule, merge with max

THE PROBLEM (in our words)
Kids stand in a line. ratings[i] is kid i's rating.
  - Every kid gets at least 1 candy.
  - A kid with a HIGHER rating than a neighbor gets MORE candy than that neighbor.
Return the minimum total candy.

RETURNS: int

EXAMPLES
  [1, 0, 2]   ->  5   (2, 1, 2)
  [1, 2, 2]   ->  4   (1, 2, 1) — equal ratings have no rule between them

CONSTRAINTS
  1 <= len(ratings) <= 20,000 (perf test: 100,000)

BEFORE YOU CODE
  Do the left-to-right sweep on [1, 3, 4, 5, 2] by hand. Is it enough? What does it get wrong?
  Then the right-to-left sweep. Why max() and not plain assignment?
"""
from typing import List

# PLAN
# RETURNS:
# Sweep 1 rule:
# Sweep 2 rule:
# Idea + Big-O:


def candy(ratings: List[int]) -> int:
    pass


# ---------- tests: don't edit below ----------
import random
from _check import check

ENTRY = "candy"
CASES = [
    (([1, 0, 2],), 5, "example"),
    (([1, 2, 2],), 4, "equal ratings"),
    (([5],), 1, "one kid"),
    (([1, 3, 4, 5, 2],), 11, "peak near the end"),
    (([5, 4, 3, 2, 1],), 15, "all falling"),
    (([1, 2, 87, 87, 87, 2, 1],), 13, "plateau"),
    (([2, 2, 2],), 3, "all equal"),
]
_r = random.Random(15)
PERF = [("100,000 kids", lambda: ([_r.randint(0, 20_000) for _ in range(100_000)],), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(candy)
