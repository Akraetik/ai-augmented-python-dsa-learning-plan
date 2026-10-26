"""
SOLUTION — Lab 1.06 H-Index (LeetCode 274)

Sort descending. Paper number (1-based) is the h being tested; its citation count is the value.
Keep going while value >= paper number. Time O(n log n).

    cites = sorted(citations, reverse=True)
    h = 0
    for i, c in enumerate(cites, start=1):
        if c >= i: h = i
        else: break
    return h

O(n) bucket version (below): h can't exceed n, so cap counts at n and bucket them.
Walk from h = n down, keeping a running total of papers with >= h citations.
"""
from typing import List


def h_index(citations: List[int]) -> int:
    n = len(citations)
    buckets = [0] * (n + 1)
    for c in citations:
        buckets[min(c, n)] += 1
    papers = 0
    for h in range(n, -1, -1):
        papers += buckets[h]
        if papers >= h:
            return h
    return 0
