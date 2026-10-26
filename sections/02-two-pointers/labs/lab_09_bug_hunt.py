"""
LAB 2.09 — Bug Hunt: Two Sum II                              Tier: Bug Hunt
Lesson 2.1 and MISTAKES.md

THE PROBLEM
two_sum_sorted(numbers, target) should return the 1-INDEXED positions [i, j] of the pair that sums to
target. numbers is sorted. Exactly one answer exists.

  [2, 7, 11, 15], 9   ->  [1, 2]

THE CODE BELOW HAS FOUR BUGS. Three match mistakes already in MISTAKES.md.
One is a NEW kind of bug, common in two-pointer code. Name it in your own words.
If you'd make it again, add it to MISTAKES.md as M8.

HOW TO DO IT
  1. Don't run it. Trace [2, 7, 11, 15], target 9, on paper.
  2. List each bug with its line and mistake ID (or "new").
  3. Fix with the smallest changes. Run the file. Explain each fix out loud.
"""
from typing import List

# BUGS I FOUND (line, what's wrong, mistake ID or "new")
# 1.
# 2.
# 3.
# 4.


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers)
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left, right]
        elif total < target:
            right -= 1
        else:
            left + 1
    return []


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "two_sum_sorted"
CASES = [
    (([2, 7, 11, 15], 9), [1, 2], "example"),
    (([2, 3, 4], 6), [1, 3], "ends"),
    (([-1, 0], -1), [1, 2], "two items"),
    (([1, 2, 3, 4, 4, 9, 56, 90], 8), [4, 5], "middle pair"),
]
PERF = [("300,000 numbers", lambda: (list(range(0, 600_000, 2)), 300_002), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(two_sum_sorted)
