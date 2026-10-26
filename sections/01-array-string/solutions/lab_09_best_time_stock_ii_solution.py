"""
SOLUTION — Lab 1.09 Best Time to Buy and Sell Stock II (LeetCode 122)
Time O(n). Space O(1).
Any climb equals the sum of its day-to-day steps. Taking every positive step can't block another
step, so the sum of all positive differences is the best total. That's why greedy is correct.
"""
from typing import List


def max_profit_ii(prices: List[int]) -> int:
    total = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            total += prices[i] - prices[i - 1]
    return total
