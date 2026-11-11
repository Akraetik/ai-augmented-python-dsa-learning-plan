"""
SOLUTION — Lab 3.02 Permutation in String (LeetCode 567)
Time O(26 · n) = O(n). Space O(1) (two 26-slot lists).
A rearrangement has the same letter counts. Slide a window of len(s1) over s2 and compare counts.
26-slot lists avoid the "count of 0 vs missing key" question.
"""


def check_inclusion(s1: str, s2: str) -> bool:
    m = len(s1)
    if m > len(s2):
        return False
    need = [0] * 26
    window = [0] * 26
    for ch in s1:
        need[ord(ch) - 97] += 1
    for i, ch in enumerate(s2):
        window[ord(ch) - 97] += 1
        if i >= m:
            window[ord(s2[i - m]) - 97] -= 1
        if window == need:
            return True
    return False
