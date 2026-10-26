"""
SOLUTION — Lab 1.20 Find the Index of the First Occurrence (LeetCode 28)
Time O(n * m) worst case. Space O(1).
Last useful start = len(haystack) - len(needle). range(... + 1) includes it.
Faster methods exist (KMP, Rabin–Karp rolling hash): O(n + m). Not needed at these sizes.
"""


def str_str(haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)
    for start in range(n - m + 1):
        j = 0
        while j < m and haystack[start + j] == needle[j]:
            j += 1
        if j == m:
            return start
    return -1
