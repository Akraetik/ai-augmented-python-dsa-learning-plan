"""
SOLUTION — Lab 1.19 Reverse Words in a String (LeetCode 151)
Way 1:  return " ".join(reversed(s.split()))
split() with no argument splits on runs of whitespace and drops empty pieces, so every spacing
case is handled. O(n) time and space.

Way 2 (below): collect words by hand, then join in reverse.
"""


def reverse_words(s: str) -> str:
    words = []
    i, n = 0, len(s)
    while i < n:
        while i < n and s[i] == " ":
            i += 1
        start = i
        while i < n and s[i] != " ":
            i += 1
        if start < i:
            words.append(s[start:i])
    return " ".join(words[::-1])
