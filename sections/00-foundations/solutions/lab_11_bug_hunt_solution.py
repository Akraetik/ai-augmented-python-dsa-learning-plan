"""
SOLUTION — Lab 0.11 Bug Hunt: First Unique Character

The four bugs:
1. `counts.get(ch, 0) + 1` computes but never saves.            -> M4. Fix: counts[ch] = counts.get(ch, 0) + 1
2. `range(1, len(s))` skips index 0.                              -> M5. Fix: range(len(s))
3. `return s[i]` returns the character, not the index.            -> M6 (and M1). Fix: return i
4. `else: return -1` gives up after the first non-unique char.    -> M7. Fix: return -1 after the loop

Time O(n), space O(1) (at most 26 letters for lowercase input).
"""
def first_unique_index(s: str) -> int:
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for i in range(len(s)):
        if counts[s[i]] == 1:
            return i
    return -1
