"""
LAB 3.06 — Minimum Size Subarray Sum                         Tier: Build
LeetCode 209 (Medium) — https://leetcode.com/problems/minimum-size-subarray-sum/
Lesson 3.3 · Pattern: variable window, shortest valid — record while valid, then shrink

THE PROBLEM (in our words)
nums holds POSITIVE integers. Return the length of the shortest run of items next to each other whose
sum is at least target. If no run works, return 0.

RETURNS: int (0 when nothing works — M6)

EXAMPLES
  target = 7,  nums = [2, 3, 1, 2, 4, 3]        ->  2   ([4, 3])
  target = 4,  nums = [1, 4, 4]                 ->  1
  target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1]  ->  0

CONSTRAINTS
  1 <= len(nums) <= 100,000,  1 <= nums[i] <= 10,000

BEFORE YOU CODE
  Where does "record" go in this template, compared to lab 03? What does best start at?
  Why would this fail if nums had negative numbers? (Lesson 3.3)
"""
from typing import List

# PLAN
# RETURNS:
# Valid when:
# Where I record (inside or after the while):
# No-answer case:
# Big-O:


def min_sub_array_len(target: int, nums: List[int]) -> int:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "min_sub_array_len"
CASES = [
    ((7, [2, 3, 1, 2, 4, 3]), 2, "example"),
    ((4, [1, 4, 4]), 1, "one item is enough"),
    ((11, [1, 1, 1, 1, 1, 1, 1, 1]), 0, "impossible"),
    ((15, [1, 2, 3, 4, 5]), 5, "needs everything"),
    ((7, [2, 1, 5, 2, 8]), 1, "big item at the end"),
    ((6, [10, 2, 3]), 1, "first item alone"),
    ((213, [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]), 8, "long run"),
]
PERF = [("100,000 items, long best window", lambda: (20_000, [1] * 100_000), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(min_sub_array_len)
