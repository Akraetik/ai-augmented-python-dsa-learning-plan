"""
LAB 1.05 — Majority Element                                  Tier: Core
LeetCode 169 (Easy) — https://leetcode.com/problems/majority-element/
Lesson 1.2 · Pattern: counting → Boyer–Moore voting

THE PROBLEM (in our words)
One value appears MORE than len(nums) // 2 times. It always exists. Return it.

RETURNS: int (the value, not its index — M1)

EXAMPLES
  [3, 2, 3]               ->  3
  [2, 2, 1, 1, 1, 2, 2]   ->  2

CONSTRAINTS
  1 <= len(nums) <= 50,000 (perf test: 100,000)

DO IT THREE WAYS (in a scratch file; submit the one you like)
  1. Count with a dict or Counter.         Big-O time? space?
  2. Sort and pick one index. Which one?   Big-O?
  3. Boyer–Moore voting, O(1) space.       Explain WHY it works in your PLAN.
"""
from typing import List

# PLAN
# RETURNS:
# Way 1 + Big-O:
# Way 2 + Big-O:
# Way 3 + why it works:


def majority_element(nums: List[int]) -> int:
    pass


# ---------- tests: don't edit below ----------
import random
from _check import check

ENTRY = "majority_element"
CASES = [
    (([3, 2, 3],), 3, "example"),
    (([2, 2, 1, 1, 1, 2, 2],), 2, "example 2"),
    (([9],), 9, "one item"),
    (([5, 5, 5, 5],), 5, "all same"),
    (([-1, 4, -1, 4, -1],), -1, "negative majority"),
    (([1, 2, 7, 7, 7],), 7, "majority at the end"),
]


def _big():
    r = random.Random(5)
    nums = [7] * 50_001 + [r.randint(-10**9, 10**9) for _ in range(49_999)]
    r.shuffle(nums)
    return (nums,)


PERF = [("100,000 items", _big, 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(majority_element)
