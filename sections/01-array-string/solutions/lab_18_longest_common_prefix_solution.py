"""
SOLUTION — Lab 1.18 Longest Common Prefix (LeetCode 14)
Time O(total characters). Space O(1) beyond the output.

Outer loop: one pass = one character POSITION (column). Inner loop: every word.
Stop when a word is too short for this column, or its letter differs from the first word's.

Neat alternative: the common prefix of the whole list equals the common prefix of
min(strs) and max(strs) (alphabetical order). Compare just those two.
"""
from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    first = strs[0]
    for col in range(len(first)):
        ch = first[col]
        for word in strs[1:]:
            if col >= len(word) or word[col] != ch:
                return first[:col]
    return first
