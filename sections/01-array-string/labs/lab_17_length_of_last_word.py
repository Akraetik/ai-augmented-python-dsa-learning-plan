"""
LAB 1.17 — Length of Last Word                               Tier: Core
LeetCode 58 (Easy) — https://leetcode.com/problems/length-of-last-word/
Lesson 1.8 · Pattern: walk backward, skip spaces, guard the index

THE PROBLEM (in our words)
s holds words and spaces. Return the length of the LAST word. There's at least one word.
There may be spaces at the end.

RETURNS: int

EXAMPLES
  "Hello World"                 ->  5
  "   fly me   to   the moon  " ->  4
  "luffy is still joyboy"       ->  6

CONSTRAINTS
  1 <= len(s) <= 10,000 (perf test: 100,000)

DO IT TWICE
  1. With split(). One line.
  2. Without split(): walk backward from the end. Guard with `i >= 0` BEFORE reading s[i].
"""

# PLAN
# RETURNS:
# Way 1:
# Way 2 steps:


def length_of_last_word(s: str) -> int:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "length_of_last_word"
CASES = [
    (("Hello World",), 5, "example"),
    (("   fly me   to   the moon  ",), 4, "trailing spaces"),
    (("luffy is still joyboy",), 6, "no trailing spaces"),
    (("a",), 1, "one letter"),
    (("day   ",), 3, "one word, trailing spaces"),
    (("   x",), 1, "leading spaces"),
]
PERF = [("100,000 chars", lambda: ("word " * 19_999 + "final" + " " * 5,), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(length_of_last_word)
