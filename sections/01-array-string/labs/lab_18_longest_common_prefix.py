"""
LAB 1.18 — Longest Common Prefix                             Tier: Core
LeetCode 14 (Easy) — https://leetcode.com/problems/longest-common-prefix/
Lesson 1.8 · Pattern: compare column by column
You've seen this one before (it's where M2 showed up). Solve it fresh. Say the loop out loud first.

THE PROBLEM (in our words)
Return the longest string that every word in strs starts with. If there isn't one, return "".

RETURNS: str

EXAMPLES
  ["flower", "flow", "flight"]   ->  "fl"
  ["dog", "racecar", "car"]      ->  ""

CONSTRAINTS
  1 <= len(strs) <= 200 (perf test: 10,000 words)
  0 <= len(strs[i]) <= 200

BEFORE YOU CODE
  Finish this sentence in your PLAN: "One pass of my OUTER loop = one ______."
  Two ways to stop: a letter differs, or ______. (M5.)
"""
from typing import List

# PLAN
# RETURNS:
# One pass of my outer loop =
# I stop when:
# Idea + Big-O:


def longest_common_prefix(strs: List[str]) -> str:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "longest_common_prefix"
CASES = [
    ((["flower", "flow", "flight"],), "fl", "example"),
    ((["dog", "racecar", "car"],), "", "no prefix"),
    ((["alone"],), "alone", "one word"),
    ((["", "abc"],), "", "empty word"),
    ((["same", "same", "same"],), "same", "all same"),
    ((["ab", "a"],), "a", "shortest word is the prefix"),
    ((["abc", "abd", "ab"],), "ab", "short word last"),
]
PERF = [("10,000 words of 200 chars", lambda: (["x" * 199 + str(i % 10) for i in range(10_000)],), 1.5)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(longest_common_prefix)
