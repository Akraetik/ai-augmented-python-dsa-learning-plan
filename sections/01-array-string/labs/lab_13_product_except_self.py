"""
LAB 1.13 — Product of Array Except Self                      Tier: Build
LeetCode 238 (Medium) — https://leetcode.com/problems/product-of-array-except-self/
Lesson 1.6 · Pattern: prefix pass × suffix pass
You've seen this one before. Solve it from a blank mind, then do the O(1)-space follow-up.

THE PROBLEM (in our words)
Return a list where answer[i] is the product of every number in nums EXCEPT nums[i].
No division. O(n) time.

RETURNS: List[int]

EXAMPLES
  [2, 3, 4, 5]        ->  [60, 40, 30, 24]
  [-1, 1, 0, -3, 3]   ->  [0, 0, 9, 0, 0]

CONSTRAINTS
  2 <= len(nums) <= 100,000

BEFORE YOU CODE
  Fill in the left-product and right-product rows for the first example by hand (Lesson 1.6).
  What does the empty product start as?
  Follow-up: O(1) extra space, not counting the output list.
"""
from typing import List

# PLAN
# RETURNS:
# Left products for [2,3,4,5]:
# Right products for [2,3,4,5]:
# Idea + Big-O:


def product_except_self(nums: List[int]) -> List[int]:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "product_except_self"
CASES = [
    (([2, 3, 4, 5],), [60, 40, 30, 24], "example"),
    (([-1, 1, 0, -3, 3],), [0, 0, 9, 0, 0], "one zero"),
    (([0, 0, 2],), [0, 0, 0], "two zeros"),
    (([1, 0, 3],), [0, 3, 0], "zero in the middle"),
    (([5, 7],), [7, 5], "two items"),
    (([-2, -3, 4],), [-12, -8, 6], "negatives"),
]
PERF = [("100,000 items", lambda: ([1, -1] * 50_000,), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(product_except_self)
