"""
LAB 0.04 — Reverse a List In Place                           Tier: Warm-up
Pattern: two pointers walking inward (preview of Section 02)
Lesson: 00.3
Similar: LeetCode 344 Reverse String — https://leetcode.com/problems/reverse-string/

THE PROBLEM
Reverse the list you're given. Change the list itself. Return nothing.
Use O(1) extra space: no new list, no slicing, no .reverse(), no reversed().

RETURNS: None. The test looks at the list after your function runs.

EXAMPLES
  [1, 2, 3, 4]   ->  list becomes [4, 3, 2, 1]
  [7]            ->  list stays [7]

CONSTRAINTS
  0 <= len(nums) <= 100,000

THINK ABOUT
  One index starts at the front. One starts at the back. When do they stop?
  Trace a 4-item list AND a 5-item list on paper. (Mistake M5 lives here.)
"""
from typing import List

# PLAN
# RETURNS:
# Example by hand (4 items, then 5 items):
# When does the loop stop?
# Idea + Big-O (time and space):


def reverse_in_place(nums: List[int]) -> None:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "reverse_in_place"
CASES = [
    (([1, 2, 3, 4],), [4, 3, 2, 1], "even length"),
    (([1, 2, 3, 4, 5],), [5, 4, 3, 2, 1], "odd length"),
    (([7],), [7], "one item"),
    (([],), [], "empty"),
    (([9, 9, 1],), [1, 9, 9], "repeats"),
]
PERF = [("100,000 items", lambda: (list(range(100_000)),), 1.0)]


def run_tests(fn):
    return check(fn, CASES, inplace=0, perf=PERF)


if __name__ == "__main__":
    run_tests(reverse_in_place)
