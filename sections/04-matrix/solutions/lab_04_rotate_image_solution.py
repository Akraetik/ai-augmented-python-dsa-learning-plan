"""
SOLUTION — Lab 4.04 Rotate Image (LeetCode 48)
Time O(n²). Space O(1).
1. Transpose in place: swap (r, c) with (c, r) only for c > r. Swapping every pair would swap each one twice.
2. Reverse each row in place.
Counterclockwise: transpose, then reverse the order of the rows (matrix.reverse()).
"""
from typing import List


def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for r in range(n):
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    for row in matrix:
        row.reverse()
