"""
LAB 3.08 — Substring with Concatenation of All Words         Tier: Stretch
LeetCode 30 (Hard) — https://leetcode.com/problems/substring-with-concatenation-of-all-words/
Lesson 3.4 · Pattern: window of word-sized pieces, once per offset 0..L-1

THE PROBLEM (in our words)
Every word in words has the same length. Return every start index in s where ALL the words appear back to
back, in any order, each used exactly as many times as it appears in words, with nothing in between.
Any order of indexes is fine.

RETURNS: List[int]

EXAMPLES
  s = "barfoothefoobarman", words = ["foo", "bar"]                         ->  [0, 9]
  s = "wordgoodgoodgoodbestword", words = ["word", "good", "best", "word"]  ->  []
  s = "barfoofoobarthefoobarman", words = ["bar", "foo", "the"]            ->  [6, 9, 12]

CONSTRAINTS
  1 <= len(s) <= 10,000,  1 <= len(words) <= 5,000,  1 <= len(words[i]) <= 30

BEFORE YOU CODE
  Why one pass per offset? Write the four steps from lesson 3.4 for one pass.
"""
from typing import List

# PLAN
# RETURNS:
# L, total words, and the offsets I try:
# Per piece: not a word → ___; too many of a word → ___; window full → ___


def find_substring(s: str, words: List[str]) -> List[int]:
    pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "find_substring"


def _same(got, expected):
    return isinstance(got, list) and sorted(got) == sorted(expected)


CASES = [
    (("barfoothefoobarman", ["foo", "bar"]), [0, 9], "example"),
    (("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]), [], "none"),
    (("barfoofoobarthefoobarman", ["bar", "foo", "the"]), [6, 9, 12], "overlapping answers"),
    (("catdogcatcat", ["cat", "dog"]), [0, 3], "lesson trace"),
    (("aaaaaa", ["aa", "aa"]), [0, 1, 2], "offsets 0 and 1"),
    (("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]), [8], "repeated word"),
    (("ab", ["abc"]), [], "word longer than s"),
    (("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo", "barr", "wing", "ding", "wing"]), [13], "not on offset 0"),
]
PERF = [("s = 10,000, 5,000 one-letter words", lambda: ("a" * 10_000, ["a"] * 5_000), 1.5)]


def run_tests(fn):
    return check(fn, CASES, compare=_same, perf=PERF)


if __name__ == "__main__":
    run_tests(find_substring)
