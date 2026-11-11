"""
SOLUTION — Lab 3.07 Minimum Window Substring (LeetCode 76)
Time O(len(s) + len(t)). Space O(distinct characters).

need = Counter(t); required = number of DIFFERENT characters in t.
have = how many of those characters the window currently satisfies.
  - a character enters and its count REACHES need[ch]  → have += 1
  - a character leaves and its count DROPS BELOW need[ch] → have -= 1
Valid when have == required. Record start and length, then shrink.
"""
from collections import Counter


def min_window(s: str, t: str) -> str:
    need = Counter(t)
    required = len(need)
    window = {}
    have = 0
    best_len, best_start = float("inf"), 0
    left = 0
    for right, ch in enumerate(s):
        window[ch] = window.get(ch, 0) + 1
        if ch in need and window[ch] == need[ch]:
            have += 1
        while have == required:
            if right - left + 1 < best_len:
                best_len, best_start = right - left + 1, left
            out = s[left]
            window[out] -= 1
            if out in need and window[out] < need[out]:
                have -= 1
            left += 1
    return "" if best_len == float("inf") else s[best_start:best_start + best_len]
