"""
LAB 1.02 — Remove Element                                    Tier: Core
LeetCode 27 (Easy) — https://leetcode.com/problems/remove-element/
Lesson 1.1 · Pattern: read/write pointers

THE PROBLEM (in our words)
Remove every copy of val from nums, in place. Return k, the number of items that are NOT val.
The first k slots of nums must hold those items (any order is accepted on LeetCode;
these tests expect the original order, which the write-pointer method gives you).
Whatever sits after slot k doesn't matter.

RETURNS: int k — and nums changed in place

EXAMPLES
  nums = [3, 2, 2, 3], val = 3        ->  k = 2, nums starts with [2, 2]
  nums = [0, 1, 2, 2, 3, 0, 4, 2], 2  ->  k = 5, nums starts with [0, 1, 3, 0, 4]

CONSTRAINTS
  0 <= len(nums) <= 100 (perf test: 100,000)

BEFORE YOU CODE
  What's the "keep rule"? Write it in one line of English.
  Why is `nums.remove(val)` in a loop a bad idea? (Lesson 00.2)
"""
from typing import List

# PLAN
# RETURNS:
# Keep rule:
# Idea + Big-O:
# Edge cases:


def remove_element(nums: List[int], val: int) -> int:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "remove_element"


def _result(args, k):
    return (k, args[0][:k] if isinstance(k, int) else None)


CASES = [
    (([3, 2, 2, 3], 3), (2, [2, 2]), "example"),
    (([0, 1, 2, 2, 3, 0, 4, 2], 2), (5, [0, 1, 3, 0, 4]), "example 2"),
    (([], 1), (0, []), "empty"),
    (([5, 5, 5], 5), (0, []), "all removed"),
    (([1, 2, 3], 9), (3, [1, 2, 3]), "none removed"),
    (([7], 7), (0, []), "one item, removed"),
]
PERF = [("300,000 items", lambda: ([i % 2 for i in range(300_000)], 1), 1.0)]


def run_tests(fn):
    return check(fn, CASES, inplace=_result, perf=PERF)


if __name__ == "__main__":
    run_tests(remove_element)
