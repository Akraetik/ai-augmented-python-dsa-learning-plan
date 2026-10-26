"""
LAB 0.03 — Count the Letters                                 Tier: Warm-up
Pattern: counting with a dict
Lesson: 00.4

THE PROBLEM
Given a string, count how many times each LETTER appears. Ignore case ("A" and "a" are the same).
Ignore anything that isn't a letter: spaces, digits, punctuation.
Return a dict that maps each lowercase letter to its count. Letters that never appear are left out.

RULE: first solve it with a plain dict and .get(). Then, once it passes, try a second version
with collections.Counter in a scratch file and compare.

RETURNS: dict[str, int]

EXAMPLES
  "Banana!"    ->  {"b": 1, "a": 3, "n": 2}
  "a1 A"       ->  {"a": 2}
  ""           ->  {}

CONSTRAINTS
  0 <= len(s) <= 100,000
"""
from typing import Dict

# PLAN
# RETURNS:
# Restate:
# Edge cases:
# Idea + Big-O:


def count_letters(s: str) -> Dict[str, int]:
    pass


# ---------- tests: don't edit below ----------
import random
import string
from _check import check

ENTRY = "count_letters"
CASES = [
    (("Banana!",), {"b": 1, "a": 3, "n": 2}, "example"),
    (("a1 A",), {"a": 2}, "case and digits"),
    (("",), {}, "empty"),
    (("123 !?",), {}, "no letters"),
    (("Zz zZ",), {"z": 4}, "mixed case"),
    (("The quick brown fox",), {"t": 1, "h": 1, "e": 1, "q": 1, "u": 1, "i": 1, "c": 1, "k": 1,
                                "b": 1, "r": 1, "o": 2, "w": 1, "n": 1, "f": 1, "x": 1}, "sentence"),
]
_r = random.Random(2)
PERF = [("100,000 chars", lambda: ("".join(_r.choice(string.ascii_letters + " ,.") for _ in range(100_000)),), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(count_letters)
