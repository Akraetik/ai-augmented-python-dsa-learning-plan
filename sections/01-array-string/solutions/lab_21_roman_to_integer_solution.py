"""
SOLUTION — Lab 1.21 Roman to Integer (LeetCode 13)
Time O(n). Space O(1).
Rule: if the NEXT symbol is bigger than this one, subtract this one; otherwise add it.
The last symbol has no next, so it's always added (the i + 1 < n guard).
"""

VALUE = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_int(s: str) -> int:
    total = 0
    n = len(s)
    for i in range(n):
        v = VALUE[s[i]]
        if i + 1 < n and VALUE[s[i + 1]] > v:
            total -= v
        else:
            total += v
    return total
