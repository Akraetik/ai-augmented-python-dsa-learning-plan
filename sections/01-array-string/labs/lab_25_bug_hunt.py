"""
LAB 1.25 — Bug Hunt: Move Zeroes                             Tier: Bug Hunt
Based on LeetCode 283 (Easy) — https://leetcode.com/problems/move-zeroes/
Lesson 1.1 and MISTAKES.md

THE PROBLEM
move_zeroes(nums) should move every 0 to the END of the list, keeping the other numbers in their
original order. In place. Return nothing.

  [0, 1, 0, 3, 12]   ->  [1, 3, 12, 0, 0]
  [0]                ->  [0]

The code below uses the read/write pointer pattern from Lesson 1.1. It has FOUR bugs.

HOW TO DO IT
  1. Don't run it. Trace [0, 1, 0, 3, 12] on paper with columns read, write, nums.
  2. List each bug with its line and the mistake ID (M1–M7) it matches.
  3. Fix with the smallest changes you can.
  4. Run the file. Then explain each fix out loud, as if to an interviewer.
"""
from typing import List

# BUGS I FOUND (line, what's wrong, mistake ID)
# 1.
# 2.
# 3.
# 4.


def move_zeroes(nums: List[int]) -> None:
    write = 0
    for read in range(1, len(nums)):
        if nums[read] != 0:
            nums[write] = read
            write + 1
    for i in range(write, len(nums)):
        nums[i] = 0
    return nums[:write]


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "move_zeroes"


def _result(args, returned):
    return (args[0], returned)


CASES = [
    (([0, 1, 0, 3, 12],), ([1, 3, 12, 0, 0], None), "example"),
    (([0],), ([0], None), "one zero"),
    (([5, 0],), ([5, 0], None), "nonzero first"),
    (([1, 2, 3],), ([1, 2, 3], None), "no zeros"),
    (([0, 0, 7],), ([7, 0, 0], None), "zeros first"),
]
PERF = [("100,000 items", lambda: ([0, 1] * 50_000,), 1.0)]


def run_tests(fn):
    return check(fn, CASES, inplace=_result, perf=PERF)


if __name__ == "__main__":
    run_tests(move_zeroes)
