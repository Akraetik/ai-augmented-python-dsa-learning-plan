"""
LAB 1.04 — Remove Duplicates from Sorted Array II            Tier: Build
LeetCode 80 (Medium) — https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
Lesson 1.1 · Pattern: read/write pointers, look back TWO kept slots

THE PROBLEM (in our words)
nums is sorted. Keep each value AT MOST TWICE, in order, in the first k slots. Return k.
O(1) extra space.

RETURNS: int k — and nums changed in place

EXAMPLES
  [1, 1, 1, 2, 2, 3]           ->  k = 5, nums starts with [1, 1, 2, 2, 3]
  [0, 0, 1, 1, 1, 1, 2, 3, 3]  ->  k = 7, nums starts with [0, 0, 1, 1, 2, 3, 3]

CONSTRAINTS
  1 <= len(nums) <= 30,000 (perf test: 100,000), sorted

BEFORE YOU CODE
  In lab 03 you compared with the last KEPT item. Here, which kept item tells you "this would be a third copy"?
  What happens for the first two items, before there are two kept slots to look back at?
  Bonus: rewrite it so the "2" is a parameter. Then lab 03 is the same function with 1.
"""
from typing import List

# PLAN
# RETURNS:
# Keep rule:
# First two items:
# Idea + Big-O:


def remove_duplicates_ii(nums: List[int]) -> int:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "remove_duplicates_ii"


def _result(args, k):
    return (k, args[0][:k] if isinstance(k, int) else None)


CASES = [
    (([1, 1, 1, 2, 2, 3],), (5, [1, 1, 2, 2, 3]), "example"),
    (([0, 0, 1, 1, 1, 1, 2, 3, 3],), (7, [0, 0, 1, 1, 2, 3, 3]), "example 2"),
    (([4],), (1, [4]), "one item"),
    (([4, 4],), (2, [4, 4]), "two same"),
    (([7, 7, 7, 7, 7],), (2, [7, 7]), "all same"),
    (([1, 2, 3],), (3, [1, 2, 3]), "no duplicates"),
    (([1, 1, 2, 2, 2, 3, 3, 3, 3],), (6, [1, 1, 2, 2, 3, 3]), "several runs"),
]
PERF = [("300,000 items", lambda: ([i // 4 for i in range(300_000)],), 1.0)]


def run_tests(fn):
    return check(fn, CASES, inplace=_result, perf=PERF)


if __name__ == "__main__":
    run_tests(remove_duplicates_ii)
