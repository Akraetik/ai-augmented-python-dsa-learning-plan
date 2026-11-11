"""
LAB 3.09 — Bug Hunt: Longest Substring Without Repeating     Tier: Bug Hunt
Lesson 3.2 and MISTAKES.md

THE PROBLEM
longest(s) should return the length of the longest run of characters with no repeats.

  "abcabcbb"  ->  3
  "pwwkew"    ->  3

The code uses the variable-window template from lesson 3.2. It has FOUR bugs.
Three match mistakes in MISTAKES.md. One is new and very common in sliding-window code.
If you'd make the new one again, add it to MISTAKES.md.

HOW TO DO IT
  1. Don't run it. Trace "pwwkew" on paper: columns right, left, seen, best.
  2. List each bug with its line and the mistake ID (or "new").
  3. Fix with the smallest changes. Run it. Explain each fix out loud.
"""

# BUGS I FOUND (line, what's wrong, mistake ID or "new")
# 1.
# 2.
# 3.
# 4.


def longest(s: str) -> int:
    seen = set()
    left = 0
    best = 0
    for right in range(len(s)):
        if s[right] in seen:
            seen.remove(s[left])
            left + 1
        seen.add(s[right])
        best = max(best, right - left)
        return best


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "longest"
CASES = [
    (("abcabcbb",), 3, "example"),
    (("pwwkew",), 3, "example 2"),
    (("bbbbb",), 1, "all same"),
    (("",), 0, "empty"),
    (("abcdeafgh",), 8, "one long run"),
]
PERF = [("100,000 chars", lambda: ("abcdefghij" * 10_000,), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(longest)
