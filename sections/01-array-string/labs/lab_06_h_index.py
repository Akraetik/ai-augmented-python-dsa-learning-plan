"""
LAB 1.06 — H-Index                                           Tier: Build
LeetCode 274 (Medium) — https://leetcode.com/problems/h-index/
Lesson 1.2 · Pattern: sort, then compare value to position (or count into buckets)

THE PROBLEM (in our words)
citations[i] is how many times paper i was cited. The h-index is the biggest h such that the
researcher has at least h papers that each have at least h citations.

RETURNS: int

EXAMPLES
  [3, 0, 6, 1, 5]  ->  3    (three papers have 3+ citations: 3, 6, 5)
  [1, 3, 1]        ->  1
  [0, 0]           ->  0

CONSTRAINTS
  1 <= len(citations) <= 5,000 (perf test: 100,000)
  0 <= citations[i] <= 1,000

BEFORE YOU CODE
  Sort the first example biggest-first. Number the papers 1, 2, 3... Draw it like Lesson 1.2.
  What's the stopping rule? Careful: paper NUMBER is the position, citations are the VALUE (M1).
  Stretch: O(n) with buckets 0..n.
"""
from typing import List

# PLAN
# RETURNS:
# Sorted example + the rule I see:
# Idea + Big-O:


def h_index(citations: List[int]) -> int:
    pass


# ---------- tests: don't edit below ----------
import random
from _check import check

ENTRY = "h_index"
CASES = [
    (([3, 0, 6, 1, 5],), 3, "example"),
    (([1, 3, 1],), 1, "example 2"),
    (([0, 0],), 0, "no citations"),
    (([100],), 1, "one big paper"),
    (([0],), 0, "one uncited paper"),
    (([4, 4, 4, 4],), 4, "all equal to n"),
    (([10, 8, 5, 4, 3],), 4, "h in the middle"),
    (([25, 8, 5, 3, 3],), 3, "ties at the boundary"),
]
_r = random.Random(6)
PERF = [("100,000 papers", lambda: ([_r.randint(0, 1000) for _ in range(100_000)],), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(h_index)
