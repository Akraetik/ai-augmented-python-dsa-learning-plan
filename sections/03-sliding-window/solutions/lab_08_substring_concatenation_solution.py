"""
SOLUTION — Lab 3.08 Substring with Concatenation of All Words (LeetCode 30)
Time O(len(s) · L) for slicing pieces. Space O(number of words).

Run one window per offset 0..L-1, stepping by L, so every possible start is covered.
In each run:
  - piece not in words → clear the window, restart after it
  - add the piece; while it now appears more often than in words → drop pieces from the left
  - window holds exactly len(words) pieces → record left, then drop the leftmost piece
"""
from collections import Counter
from typing import List


def find_substring(s: str, words: List[str]) -> List[int]:
    L = len(words[0])
    total = len(words)
    need = Counter(words)
    out = []
    for offset in range(L):
        left = offset
        window = Counter()
        count = 0
        for right in range(offset, len(s) - L + 1, L):
            piece = s[right:right + L]
            if piece not in need:
                window.clear()
                count = 0
                left = right + L
                continue
            window[piece] += 1
            count += 1
            while window[piece] > need[piece]:
                window[s[left:left + L]] -= 1
                count -= 1
                left += L
            if count == total:
                out.append(left)
                window[s[left:left + L]] -= 1
                count -= 1
                left += L
    return out
