"""
LAB 1.01 — Merge Sorted Array                                Tier: Core
LeetCode 88 (Easy) — https://leetcode.com/problems/merge-sorted-array/
Lesson 1.1 · Pattern: three pointers, fill from the back

THE PROBLEM (in our words)
nums1 holds m sorted numbers followed by n empty slots (filled with 0s).
nums2 holds n sorted numbers.
Merge nums2 into nums1 so that all m + n slots of nums1 are sorted.

RETURNS: None. Change nums1 in place. (Read that twice. M6.)

EXAMPLES
  nums1 = [2, 5, 9, 0, 0], m = 3, nums2 = [3, 7], n = 2   ->  nums1 becomes [2, 3, 5, 7, 9]
  nums1 = [0], m = 0, nums2 = [4], n = 1                  ->  nums1 becomes [4]

CONSTRAINTS
  len(nums1) == m + n,  0 <= m, n <= 200 (perf test uses far more)
  both parts sorted, non-decreasing

BEFORE YOU CODE
  - Why does filling from the FRONT go wrong? Show it with the first example.
  - When nums2 runs out first, is there anything left to do? When nums1 runs out first?
  - Follow-up: O(m + n) time, O(1) extra space.
"""
from typing import List

# PLAN
# RETURNS:
# Restate:
# Example by hand:
# Edge cases:
# Brute force + Big-O:
# Better idea + Big-O:


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "merge"
CASES = [
    (([2, 5, 9, 0, 0], 3, [3, 7], 2), [2, 3, 5, 7, 9], "example"),
    (([0], 0, [4], 1), [4], "nums1 empty"),
    (([1], 1, [], 0), [1], "nums2 empty"),
    (([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3), [1, 2, 3, 4, 5, 6], "nums2 all smaller"),
    (([1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3), [1, 2, 3, 4, 5, 6], "nums2 all bigger"),
    (([1, 1, 3, 0, 0], 3, [1, 2], 2), [1, 1, 1, 2, 3], "duplicates"),
    (([-3, 0, 0], 1, [-5, 2], 2), [-5, -3, 2], "negatives"),
]
_A = list(range(0, 200_000, 2))
_B = list(range(1, 200_000, 2))
PERF = [("100,000 + 100,000", lambda: (_A + [0] * len(_B), len(_A), list(_B), len(_B)), 1.0)]


def run_tests(fn):
    return check(fn, CASES, inplace=0, perf=PERF)


if __name__ == "__main__":
    run_tests(merge)
