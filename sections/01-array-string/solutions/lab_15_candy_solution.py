"""
SOLUTION — Lab 1.15 Candy (LeetCode 135)
Time O(n). Space O(n).

Sweep 1 (left → right): if rated higher than the LEFT neighbor, get one more than them.
Sweep 2 (right → left): if rated higher than the RIGHT neighbor, need at least one more than them.
Use max() so sweep 2 never undoes what sweep 1 required.
Equal neighbors have no rule, so they can drop back to 1.
"""
from typing import List


def candy(ratings: List[int]) -> int:
    n = len(ratings)
    give = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            give[i] = give[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            give[i] = max(give[i], give[i + 1] + 1)
    return sum(give)
