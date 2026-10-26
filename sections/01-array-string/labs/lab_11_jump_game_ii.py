"""
LAB 1.11 — Jump Game II                                      Tier: Build
LeetCode 45 (Medium) — https://leetcode.com/problems/jump-game-ii/
Lesson 1.5 · Pattern: count "rings" (BFS by levels, with no queue)

THE PROBLEM (in our words)
Same jump rules as lab 10. This time you're promised the last index is reachable.
Return the FEWEST jumps needed to land on it.

RETURNS: int

EXAMPLES
  [2, 3, 1, 1, 4]   ->  2   (0 → 1 → 4)
  [2, 3, 0, 1, 4]   ->  2
  [0]               ->  0

CONSTRAINTS
  1 <= len(nums) <= 10,000 (perf test: 100,000)
  the end is always reachable

BEFORE YOU CODE
  Name your three variables (Lesson 1.5): jumps, end of current ring, farthest for next ring.
  When exactly do you add a jump? Why loop only to len(nums) - 1?
"""
from typing import List

# PLAN
# RETURNS:
# My three variables:
# When I count a jump:
# Idea + Big-O:


def jump(nums: List[int]) -> int:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "jump"
CASES = [
    (([2, 3, 1, 1, 4],), 2, "example"),
    (([2, 3, 0, 1, 4],), 2, "example 2"),
    (([0],), 0, "already there"),
    (([1, 2],), 1, "one jump"),
    (([1, 1, 1, 1],), 3, "step by step"),
    (([10, 1, 1, 1],), 1, "one big jump"),
    (([1, 2, 1, 1, 1],), 3, "greedy farthest isn't biggest number"),
]
PERF = [
    ("100,000 ones", lambda: ([1] * 100_000,), 1.0),
    ("100,000 twos", lambda: ([2] * 100_000,), 1.0),
]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(jump)
