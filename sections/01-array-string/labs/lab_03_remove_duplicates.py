"""
LAB 1.03 — Remove Duplicates from Sorted Array               Tier: Core
LeetCode 26 (Easy) — https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Lesson 1.1 · Pattern: read/write pointers on a sorted list
You've seen this one before (LeetCode 75 practice). Solve it from a BLANK mind. No peeking at old code.

THE PROBLEM (in our words)
nums is sorted. Keep one copy of each value, in order, in the first k slots. Return k.

RETURNS: int k — and nums changed in place

EXAMPLES
  [1, 1, 2]                       ->  k = 2, nums starts with [1, 2]
  [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]  ->  k = 5, nums starts with [0, 1, 2, 3, 4]

CONSTRAINTS
  1 <= len(nums) <= 30,000 (perf test: 100,000), sorted non-decreasing

BEFORE YOU CODE
  Keep rule: compare the current item with WHICH earlier item? nums[read - 1] or nums[write - 1]?
  Both pass here. Decide which one you'd need for lab 04 (each value up to twice), and use that one now.
"""
from typing import List

# PLAN
# RETURNS:
# Keep rule (and which neighbor I compare to):
# Idea + Big-O:


def remove_duplicates(nums: List[int]) -> int:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "remove_duplicates"


def _result(args, k):
    return (k, args[0][:k] if isinstance(k, int) else None)


CASES = [
    (([1, 1, 2],), (2, [1, 2]), "example"),
    (([0, 0, 1, 1, 1, 2, 2, 3, 3, 4],), (5, [0, 1, 2, 3, 4]), "example 2"),
    (([5],), (1, [5]), "one item"),
    (([2, 2, 2, 2],), (1, [2]), "all same"),
    (([1, 2, 3],), (3, [1, 2, 3]), "no duplicates"),
    (([-3, -3, -1, 0, 0],), (3, [-3, -1, 0]), "negatives"),
]
PERF = [("300,000 items", lambda: ([i // 2 for i in range(300_000)],), 1.0)]


def run_tests(fn):
    return check(fn, CASES, inplace=_result, perf=PERF)


if __name__ == "__main__":
    run_tests(remove_duplicates)
