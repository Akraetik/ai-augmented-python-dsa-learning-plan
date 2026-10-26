"""
LAB 1.24 — Text Justification                                Tier: Stretch
LeetCode 68 (Hard) — https://leetcode.com/problems/text-justification/
Lesson 1.8 · Pattern: greedy line packing + careful bookkeeping with helpers

THE PROBLEM (in our words)
Lay out words into lines that are exactly max_width characters wide.
  - Pack as many words as fit on each line (one space minimum between words).
  - Spread a line's extra spaces between its words as evenly as possible.
    If they don't split evenly, the LEFT gaps get the extra spaces.
  - A line with one word: the word, then spaces to fill the width.
  - The LAST line: words separated by single spaces, then spaces to fill the width.

RETURNS: List[str], every string exactly max_width long

EXAMPLE
  words = ["This", "is", "an", "example", "of", "text", "justification."], max_width = 16
  ->
  ["This    is    an",
   "example  of text",
   "justification.  "]

CONSTRAINTS
  every word is non-empty and at most max_width long

BEFORE YOU CODE
  Write three helpers first (Lesson 1.8). Test each in a scratch file.
  Use divmod(total_spaces, gaps) to get spaces-per-gap and how many gaps get +1.
"""
from typing import List

# PLAN
# RETURNS:
# Helper 1 (which words fit):
# Helper 2 (justify a full line):
# Helper 3 (last line / one word):


def full_justify(words: List[str], max_width: int) -> List[str]:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "full_justify"
CASES = [
    ((["This", "is", "an", "example", "of", "text", "justification."], 16),
     ["This    is    an", "example  of text", "justification.  "], "example"),
    ((["What", "must", "be", "acknowledgment", "shall", "be"], 16),
     ["What   must   be", "acknowledgment  ", "shall be        "], "one-word line in the middle"),
    ((["a"], 1), ["a"], "tiny"),
    ((["a", "b", "c", "d"], 3), ["a b", "c d"], "exact fit, last line"),
    ((["Listen", "to", "many,", "speak", "to", "a", "few."], 6),
     ["Listen", "to    ", "many, ", "speak ", "to   a", "few.  "], "narrow"),
    ((["one", "two", "three"], 20), ["one two three       "], "only the last line"),
]
PERF = [("20,000 words", lambda: (["word", "a", "longer", "xy"] * 5_000, 30), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(full_justify)
