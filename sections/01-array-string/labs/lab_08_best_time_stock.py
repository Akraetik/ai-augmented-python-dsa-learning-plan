"""
LAB 1.08 — Best Time to Buy and Sell Stock                   Tier: Core
LeetCode 121 (Easy) — https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Lesson 1.4 · Pattern: one pass, track the lowest price so far

THE PROBLEM (in our words)
prices[i] is a stock's price on day i. Buy on one day, sell on a LATER day. One trade only.
Return the biggest profit. If no trade makes money, return 0.

RETURNS: int

EXAMPLES
  [7, 1, 5, 3, 6, 4]   ->  5    (buy at 1, sell at 6)
  [7, 6, 4, 3, 1]      ->  0

CONSTRAINTS
  1 <= len(prices) <= 100,000

BEFORE YOU CODE
  Close Lesson 1.4. Write it from memory. Then compare.
  Why does the perf test fail the "every pair" version?
"""
from typing import List

# PLAN
# RETURNS:
# Two things I track:
# Idea + Big-O:


def max_profit(prices: List[int]) -> int:
    pass


# ---------- tests: don't edit below ----------
import random
from _check import check

ENTRY = "max_profit"
CASES = [
    (([7, 1, 5, 3, 6, 4],), 5, "example"),
    (([7, 6, 4, 3, 1],), 0, "always falling"),
    (([5],), 0, "one day"),
    (([1, 2],), 1, "two days, rising"),
    (([3, 3, 3],), 0, "flat"),
    (([2, 4, 1, 7],), 6, "new low later wins"),
    (([2, 9, 1, 3],), 7, "early pair wins"),
]
_r = random.Random(8)
PERF = [("100,000 days", lambda: ([_r.randint(1, 10_000) for _ in range(100_000)],), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(max_profit)
