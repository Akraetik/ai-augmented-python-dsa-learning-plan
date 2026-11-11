"""
SOLUTION — Lab 3.05 Longest Repeating Character Replacement (LeetCode 424)
Time O(26 · n) = O(n). Space O(1).
Changes needed = window length − count of the most common letter. Shrink while that's more than k.

The famous shortcut: keep `top`, the highest count EVER seen, and never lower it. Then the check is
(window length − top) > k, and the window shrinks by at most one per step. It still gives the right
answer because the result only grows when a window beats the old best `top`, and stale `top` values
can only make the window keep its size, never report a longer one that doesn't exist. Learn the simple
version first. Use the shortcut only if you can explain that sentence.
"""


def character_replacement(s: str, k: int) -> int:
    counts = [0] * 26
    left = 0
    best = 0
    for right, ch in enumerate(s):
        counts[ord(ch) - 65] += 1
        while (right - left + 1) - max(counts) > k:
            counts[ord(s[left]) - 65] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
