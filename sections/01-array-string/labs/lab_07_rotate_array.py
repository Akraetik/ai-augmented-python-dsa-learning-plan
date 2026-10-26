"""
LAB 1.07 — Rotate Array                                      Tier: Build
LeetCode 189 (Medium) — https://leetcode.com/problems/rotate-array/
Lesson 1.3 · Pattern: modulo index math, then three reversals

THE PROBLEM (in our words)
Rotate nums to the RIGHT by k steps, in place. Items pushed off the end wrap to the front.

RETURNS: None. Change nums in place. (`nums = ...` does NOT count. Lesson 1.3, "The in-place trap.")

EXAMPLES
  [1, 2, 3, 4, 5, 6, 7], k = 3   ->  [5, 6, 7, 1, 2, 3, 4]
  [-1, -100, 3, 99], k = 2       ->  [3, 99, -1, -100]

CONSTRAINTS
  1 <= len(nums) <= 100,000
  0 <= k <= 100,000   (k can be BIGGER than len(nums))

DO IT TWICE
  1. With an extra list: item i goes to (i + k) % n. Then copy back into nums.   O(n) space.
  2. Three reversals. O(1) space. Write a helper reverse(nums, left, right).
"""
from typing import List

# PLAN
# RETURNS:
# What to do with k first:
# Way 1:
# Way 2 (the three calls):


def rotate(nums: List[int], k: int) -> None:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "rotate"
CASES = [
    (([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4], "example"),
    (([-1, -100, 3, 99], 2), [3, 99, -1, -100], "example 2"),
    (([1, 2, 3], 0), [1, 2, 3], "k = 0"),
    (([1, 2, 3], 3), [1, 2, 3], "k = n"),
    (([1, 2, 3], 4), [3, 1, 2], "k > n"),
    (([9], 100), [9], "one item, huge k"),
    (([1, 2], 1), [2, 1], "two items"),
]
PERF = [
    ("100,000 items, k = 54,321", lambda: (list(range(100_000)), 54_321), 1.0),
    ("100,000 items, k = 99,999", lambda: (list(range(100_000)), 99_999), 1.0),
]


def run_tests(fn):
    return check(fn, CASES, inplace=0, perf=PERF)


if __name__ == "__main__":
    run_tests(rotate)
