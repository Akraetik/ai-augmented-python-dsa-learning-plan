"""
SOLUTION — Lab 1.08 Best Time to Buy and Sell Stock (LeetCode 121)
Time O(n). Space O(1).
Track the lowest price so far (the best day to have bought). At each day, the best sale today is
price - lowest. Keep the best of those. best starts at 0, so falling prices return 0.
"""
from typing import List


def max_profit(prices: List[int]) -> int:
    lowest = float("inf")
    best = 0
    for p in prices:
        lowest = min(lowest, p)
        best = max(best, p - lowest)
    return best
