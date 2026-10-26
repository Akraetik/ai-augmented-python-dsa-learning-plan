"""
LAB 1.12 — Gas Station                                       Tier: Build
LeetCode 134 (Medium) — https://leetcode.com/problems/gas-station/
Lesson 1.5 · Pattern: total check + reset the start when the running tank goes negative

THE PROBLEM (in our words)
Stations sit in a circle. At station i you pick up gas[i]. Driving from i to i + 1 burns cost[i].
The last station leads back to station 0. Your tank starts empty.
Return the index of the station where you can start and drive the full circle. If none works, return -1.
If one works, it's the only one.

RETURNS: int (an index, or -1)

EXAMPLES
  gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2]   ->  3
  gas = [2, 3, 4],       cost = [3, 4, 3]         ->  -1

CONSTRAINTS
  1 <= n <= 100,000

BEFORE YOU CODE
  Write Lesson 1.5's "Fact 2" in your own words. Why can you skip every station between the old start and the failure?
"""
from typing import List

# PLAN
# RETURNS:
# Fact 1:
# Fact 2 (my words):
# Idea + Big-O:


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "can_complete_circuit"
CASES = [
    (([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3, "example"),
    (([2, 3, 4], [3, 4, 3]), -1, "impossible"),
    (([5], [4]), 0, "one station"),
    (([4], [5]), -1, "one station, not enough"),
    (([3, 1, 1], [1, 2, 2]), 0, "start at 0"),
    (([1, 1, 3], [2, 2, 1]), 2, "start at the end"),
    (([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]), 4, "wraps around"),
]


def _long_runs():
    n = 100_000
    gas, cost = [1] * n, [1] * n
    cost[n - 2] = 2   # every early start drives almost the whole way, then fails here
    gas[n - 1] = 2    # the only good start is the last station
    return (gas, cost)


PERF = [
    ("100,000 stations, impossible", lambda: ([1] * 99_999 + [100_000], [2] * 100_000), 1.0),
    ("100,000 stations, answer is last", _long_runs, 1.0),
]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(can_complete_circuit)
