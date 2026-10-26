"""
SOLUTION — Lab 1.17 Length of Last Word (LeetCode 58)
Way 1:  return len(s.split()[-1])           O(n) time, O(n) space.
Way 2 (below): walk back over trailing spaces, then count letters. O(n) time, O(1) space.
`i >= 0` comes first in each `and` so s[i] is never read at i = -1.
"""


def length_of_last_word(s: str) -> int:
    i = len(s) - 1
    while i >= 0 and s[i] == " ":
        i -= 1
    length = 0
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1
    return length
