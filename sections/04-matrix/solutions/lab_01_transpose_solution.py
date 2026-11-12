"""
SOLUTION — Lab 4.01 Transpose Matrix (LeetCode 867)
Time O(m · n). Space O(m · n) for the output.
One-liner: [list(row) for row in zip(*matrix)]   (*matrix passes each row as a separate argument;
zip groups their first items, then their second items, and so on: those are the columns.)
"""
from typing import List


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    rows, cols = len(matrix), len(matrix[0])
    out = [[0] * rows for _ in range(cols)]
    for r in range(rows):
        for c in range(cols):
            out[c][r] = matrix[r][c]
    return out
