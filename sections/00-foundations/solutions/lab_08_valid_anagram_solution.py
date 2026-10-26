"""
SOLUTION — Lab 0.08 Valid Anagram (LeetCode 242)

Way 1, sorting:   return sorted(s) == sorted(t)      O(n log n) time.
Way 2, counting:  return Counter(s) == Counter(t)    O(n) time, O(1) space (26 letters).

Quick reject: different lengths can't be anagrams. Check it first.

The version below counts by hand with one dict: add for s, subtract for t, all zero means anagram.
"""
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in t:
        if counts.get(ch, 0) == 0:
            return False
        counts[ch] -= 1
    return True
