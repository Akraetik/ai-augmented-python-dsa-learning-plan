"""
LAB 0.11 — Bug Hunt: First Unique Character                  Tier: Bug Hunt
Based on LeetCode 387 (Easy) — https://leetcode.com/problems/first-unique-character-in-a-string/
Lesson: 00.5 and MISTAKES.md

THE PROBLEM
first_unique_index(s) should return the INDEX of the first character that appears exactly once in s.
If there is none, return -1.

  "leetcode"   ->  0    ('l' appears once)
  "loveleetcode"  ->  2    ('v' is the first that appears once)
  "aabb"       ->  -1

THE CODE BELOW HAS FOUR BUGS. Each one is a mistake from MISTAKES.md.
Interviewers run this kind of round in 2026: "here's broken code, find the bugs, talk me through it."

HOW TO DO IT
  1. Don't run it yet. Read it. Trace "loveleetcode" on paper.
  2. Write each bug you find in the BUGS list below, with the mistake ID (M1-M7).
  3. Fix them. Change as little as possible.
  4. Run the file.
"""

# BUGS I FOUND (line, what's wrong, mistake ID)
# 1.
# 2.
# 3.
# 4.


def first_unique_index(s: str) -> int:
    counts = {}
    for ch in s:
        counts.get(ch, 0) + 1
    for i in range(1, len(s)):
        if counts[s[i]] == 1:
            return s[i]
        else:
            return -1


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "first_unique_index"
CASES = [
    (("leetcode",), 0, "unique at index 0"),
    (("loveleetcode",), 2, "unique in the middle"),
    (("aabb",), -1, "none"),
    (("z",), 0, "one char"),
    (("aabbc",), 4, "unique at the end"),
]
PERF = [("100,000 chars", lambda: ("ab" * 50_000 + "c",), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(first_unique_index)
