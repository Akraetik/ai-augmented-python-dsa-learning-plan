"""
LAB 3.03 — Longest Substring Without Repeating Characters    Tier: Build
LeetCode 3 (Medium) — https://leetcode.com/problems/longest-substring-without-repeating-characters/
Lesson 3.2 · Pattern: variable window, longest valid — shrink while a letter repeats

THE PROBLEM (in our words)
Return the length of the longest run of characters in s with no character appearing twice.

RETURNS: int (a length, not the substring — M6)

EXAMPLES
  "abcabcbb"   ->  3   ("abc")
  "bbbbb"      ->  1
  "pwwkew"     ->  3   ("wke")
  ""           ->  0

CONSTRAINTS
  0 <= len(s) <= 50,000 on LeetCode. The perf test uses 100,000 characters and thousands of
  DIFFERENT characters, so "extend each start until a repeat" is too slow here.

BEFORE YOU CODE
  Write the three steps (grow / shrink while broken / record) for this problem.
  Trace "dvdf" and "abba". Both catch common bugs.
"""

# PLAN
# RETURNS:
# Grow:
# Broken when:
# Shrink:
# Record:


def length_of_longest_substring(s: str) -> int:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "length_of_longest_substring"
CASES = [
    (("abcabcbb",), 3, "example"),
    (("bbbbb",), 1, "all same"),
    (("pwwkew",), 3, "answer in the middle"),
    (("",), 0, "empty"),
    (("dvdf",), 3, "shrink just past the old copy"),
    (("abba",), 2, "left must never move back"),
    ((" ",), 1, "a space counts"),
    (("tmmzuxt",), 5, "repeat far back"),
]


def _big():
    chars = [chr(0x4E00 + i) for i in range(20_000)]
    return ("".join(chars[i % 20_000] for i in range(100_000)),)


PERF = [("100,000 chars, 20,000 different", _big, 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(length_of_longest_substring)
