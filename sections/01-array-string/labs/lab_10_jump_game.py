"""
LAB 1.10 — Jump Game                                         Tier: Build
LeetCode 55 (Medium) — https://leetcode.com/problems/jump-game/
Lesson 1.5 · Pattern: track the farthest reach

THE PROBLEM (in our words)
You start at index 0. nums[i] is the MOST you can jump forward from index i (any distance from 0 up to it).
Return True if you can land on the last index.

RETURNS: bool

EXAMPLES
  [2, 3, 1, 1, 4]   ->  True
  [3, 2, 1, 0, 4]   ->  False   (every path lands on the 0 at index 3)

CONSTRAINTS
  1 <= len(nums) <= 10,000 (perf test: 100,000)
  0 <= nums[i] <= 100,000

BEFORE YOU CODE
  Trace both examples with a `reach` column, like Lesson 1.5.
  What's the exact test for "stuck"? What's the exact test for "made it"? (M5: last index is len - 1.)
"""
from typing import List

# PLAN
# RETURNS:
# Stuck when:
# Made it when:
# Idea + Big-O:


def can_jump(nums: List[int]) -> bool:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "can_jump"
CASES = [
    (([2, 3, 1, 1, 4],), True, "example"),
    (([3, 2, 1, 0, 4],), False, "wall of zero"),
    (([0],), True, "already at the end"),
    (([0, 1],), False, "stuck at start"),
    (([1, 0, 1],), False, "zero in the middle"),
    (([2, 0, 0],), True, "jump over zeros"),
    (([1, 1, 1, 1],), True, "step by step"),
    (([5, 0, 0, 0, 0, 0, 1],), False, "just short"),
]
PERF = [
    ("100,000 ones", lambda: ([1] * 100_000,), 1.0),
    ("100,000, blocked at end", lambda: ([1] * 99_998 + [0, 1],), 1.0),
]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(can_jump)
