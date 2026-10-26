"""
LAB 1.09 — Best Time to Buy and Sell Stock II                Tier: Build
LeetCode 122 (Medium) — https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Lesson 1.4 · Pattern: greedy — collect every rise

THE PROBLEM (in our words)
Same prices list. Now you may trade as many times as you like, but you hold at most one share at a time.
(You can sell and buy again on the same day.) Return the biggest total profit.

RETURNS: int

EXAMPLES
  [7, 1, 5, 3, 6, 4]   ->  7    (1→5 is 4, then 3→6 is 3)
  [1, 2, 3, 4, 5]      ->  4    (one long climb, or four small steps — same total)
  [7, 6, 4, 3, 1]      ->  0

CONSTRAINTS
  1 <= len(prices) <= 30,000 (perf test: 100,000)

BEFORE YOU CODE
  Draw the second example as a line. Is 1→5 the same as 1→2 + 2→3 + 3→4 + 4→5?
  Write one sentence: why is greedy correct here?
"""
from typing import List

# PLAN
# RETURNS:
# Why greedy works (one sentence):
# Idea + Big-O:


def max_profit_ii(prices: List[int]) -> int:
    pass


# ---------- tests: don't edit below ----------
import random
from _check import check

ENTRY = "max_profit_ii"
CASES = [
    (([7, 1, 5, 3, 6, 4],), 7, "example"),
    (([1, 2, 3, 4, 5],), 4, "one climb"),
    (([7, 6, 4, 3, 1],), 0, "always falling"),
    (([5],), 0, "one day"),
    (([2, 1, 2, 1, 2],), 2, "zigzag"),
    (([3, 3, 5, 0, 0, 3, 1, 4],), 8, "plateaus"),
]
_r = random.Random(9)
PERF = [("100,000 days", lambda: ([_r.randint(1, 10_000) for _ in range(100_000)],), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(max_profit_ii)
