"""
SOLUTION — Lab 2.02 Is Subsequence (LeetCode 392)
Time O(len(t)). Space O(1).
j walks t every step. i walks s only on a match. All of s matched → True.
Greedy is safe: matching a character at its earliest spot leaves the most of t for the rest.
"""


def is_subsequence(s: str, t: str) -> bool:
    i = 0
    for ch in t:
        if i < len(s) and ch == s[i]:
            i += 1
    return i == len(s)
