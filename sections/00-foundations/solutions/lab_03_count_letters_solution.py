"""
SOLUTION — Lab 0.03 Count the Letters
Time O(n), space O(1) (at most 26 keys).

Key idea: one pass. Skip non-letters. Lower-case the rest. Count with .get(key, 0) + 1.

Pitfall (M4): `counts.get(ch, 0) + 1` alone does nothing. You must assign it back.

Counter version, for comparison:
    from collections import Counter
    return dict(Counter(ch.lower() for ch in s if ch.isalpha()))
"""
from typing import Dict


def count_letters(s: str) -> Dict[str, int]:
    counts = {}
    for ch in s:
        if ch.isalpha():
            ch = ch.lower()
            counts[ch] = counts.get(ch, 0) + 1
    return counts
