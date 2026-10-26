"""
LAB 0.05 — Contains Duplicate                                Tier: Core
LeetCode 217 (Easy) — https://leetcode.com/problems/contains-duplicate/
Pattern: "have I seen this before?" -> set
Lesson: 00.4

THE PROBLEM (in our words)
Return True if any value shows up at least twice in the list. Return False if every value is different.

RETURNS: bool

EXAMPLES
  [4, 7, 1, 7]   ->  True
  [4, 7, 1]      ->  False

CONSTRAINTS
  1 <= len(nums) <= 100,000
  values fit in a normal int

THINK ABOUT
  Write the brute force in your PLAN first. What's its Big-O?
  The perf test uses 100,000 different numbers. Will your brute force survive? (Lesson 00.2 table.)
  Then: which tool answers "have I seen this?" in O(1)?
"""
from typing import List

# PLAN
# RETURNS:
# Brute force + Big-O:
# Better idea + Big-O:
# Edge cases:


def contains_duplicate(nums: List[int]) -> bool:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "contains_duplicate"
CASES = [
    (([4, 7, 1, 7],), True, "example"),
    (([4, 7, 1],), False, "all different"),
    (([5],), False, "one item"),
    (([2, 2],), True, "pair"),
    (([-1, 0, 1, -1],), True, "negatives"),
    (([1, 2, 3, 4, 5, 6, 7, 8, 9, 1],), True, "dup at the ends"),
]
PERF = [
    ("100,000 unique", lambda: (list(range(100_000)),), 1.0),
    ("dup at very end", lambda: (list(range(100_000)) + [0],), 1.0),
]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(contains_duplicate)
