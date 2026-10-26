"""
LAB 0.09 — Two Sum                                           Tier: Core
LeetCode 1 (Easy) — https://leetcode.com/problems/two-sum/
Pattern: dict of value -> index ("what number do I still need?")
Lesson: 00.4

THE PROBLEM (in our words)
Find the two positions whose values add up to target. Return their indexes as a list [i, j] with i < j.
There is exactly one answer. You can't use the same position twice.

RETURNS: List[int] of two INDEXES (not values — Mistake M1)

EXAMPLES
  nums = [8, 2, 11, 5], target = 7    ->  [1, 3]     because 2 + 5 = 7
  nums = [3, 3], target = 6           ->  [0, 1]

CONSTRAINTS
  2 <= len(nums) <= 30,000
  exactly one valid answer

THINK ABOUT
  Brute force tries every pair. Big-O?
  Better: when you stand on value x, what number would complete the pair? Where could you
  have stored the numbers you already walked past, so you can check in O(1)?
  Careful with [3, 3], target 6: don't match a position with itself.
"""
from typing import List

# PLAN
# RETURNS:
# Brute force + Big-O:
# Better idea + Big-O:
# What goes in the dict (key -> value)?:


def two_sum(nums: List[int], target: int) -> List[int]:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "two_sum"
CASES = [
    (([8, 2, 11, 5], 7), [1, 3], "example"),
    (([3, 3], 6), [0, 1], "same value twice"),
    (([3, 2, 4], 6), [1, 2], "don't reuse index 0"),
    (([-4, 10, 1, 9], 5), [0, 3], "negatives"),
    (([0, 7, 0], 0), [0, 2], "zeros"),
]
PERF = [("30,000 items, answer at the end",
         lambda: (list(range(1, 30_000)) + [-5, 10**9], 10**9 - 5), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(two_sum)
