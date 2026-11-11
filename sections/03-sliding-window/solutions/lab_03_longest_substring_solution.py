"""
SOLUTION — Lab 3.03 Longest Substring Without Repeating Characters (LeetCode 3)
Time O(n). Space O(number of distinct characters).

Set version (the template):
    seen = set(); left = best = 0
    for right, ch in enumerate(s):
        while ch in seen:
            seen.remove(s[left]); left += 1
        seen.add(ch)
        best = max(best, right - left + 1)

Jump version (below): remember each character's last index and jump left straight past it.
The max() keeps left from moving backward ("abba": the old 'a' is already outside the window).
"""


def length_of_longest_substring(s: str) -> int:
    last = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last:
            left = max(left, last[ch] + 1)
        last[ch] = right
        best = max(best, right - left + 1)
    return best
