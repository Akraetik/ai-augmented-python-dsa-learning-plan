"""
LAB 2.07 — Trapping Rain Water, Two Pointers                 Tier: Stretch
LeetCode 42 (Hard) — https://leetcode.com/problems/trapping-rain-water/
Lesson 2.5 · Pattern: two pointers from the ends; process the side with the smaller max

THE PROBLEM
Same as lab 1.14. This time: O(1) extra space. No max_left / max_right lists.
This lab MEASURES your extra memory on a 100,000-bar input.

RETURNS: int

EXAMPLES
  [2, 0, 3, 1, 4, 2]                     ->  4
  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]   ->  6

BEFORE YOU CODE
  Re-trace the table in lesson 2.5 by hand. Then close it and write the loop.
"""
from typing import List

# PLAN
# RETURNS:
# Variables I keep:
# Which side I process each step, and why its water level is known:


def trap(height: List[int]) -> int:
    pass


# ---------- tests: don't edit below ----------
import random
import tracemalloc
from _check import check

ENTRY = "trap"
CASES = [
    (([2, 0, 3, 1, 4, 2],), 4, "lesson picture"),
    (([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],), 6, "classic"),
    (([4, 2, 0, 3, 2, 5],), 9, "deep middle"),
    (([5],), 0, "one bar"),
    (([1, 2, 3, 4],), 0, "staircase up"),
    (([3, 0, 3],), 3, "one pit"),
    (([5, 4, 1, 2],), 1, "falls then small rise"),
]
_r = random.Random(42)
_BIG = [_r.randint(0, 100_000) for _ in range(100_000)]
PERF = [("100,000 bars", lambda: (list(_BIG),), 1.0)]


def _memory_ok(fn):
    data = list(_BIG)
    tracemalloc.start()
    fn(data)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    ok = peak < 50_000
    print(("PASS" if ok else "FAIL") + f" extra memory: {peak / 1000:.0f} KB (limit 50 KB)"
          + ("" if ok else " — two lists of 100,000 ints use ~1,600 KB. Use a few variables instead."))
    return ok


def run_tests(fn):
    ok = check(fn, CASES, perf=PERF)
    return _memory_ok(fn) and ok if ok else False


if __name__ == "__main__":
    run_tests(trap)
