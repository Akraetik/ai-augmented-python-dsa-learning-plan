"""
SOLUTION — Lab 1.12 Gas Station (LeetCode 134)
Time O(n). Space O(1).

Fact 1: if total gas < total cost, no start works.
Fact 2: if starting at s you run dry before reaching j, then no start between s and j works either:
each of them would begin with an empty tank, which is never better than arriving with >= 0.
So when the running tank goes negative at i, the next possible start is i + 1.
If Fact 1 passes, the last start chosen is the answer.
"""
from typing import List


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    start, tank = 0, 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start
