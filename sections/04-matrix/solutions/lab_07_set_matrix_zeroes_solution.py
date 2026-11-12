"""
SOLUTION — Lab 4.07 Set Matrix Zeroes (LeetCode 73)
Time O(m · n). Space O(1).

Two-set version (O(m + n) space, a fine first answer):
    zr = {r for r in range(m) for c in range(n) if matrix[r][c] == 0}
    zc = {c for r in range(m) for c in range(n) if matrix[r][c] == 0}
    for r in range(m):
        for c in range(n):
            if r in zr or c in zc: matrix[r][c] = 0

O(1) version (below): row 0 and column 0 hold the flags.
1. Remember whether row 0 / column 0 had a zero of their own.
2. For inner cells that are 0, mark matrix[r][0] and matrix[0][c].
3. Zero inner cells whose row flag or column flag is 0.
4. Zero row 0 and column 0 last, from the remembered booleans.
"""
from typing import List


def set_zeroes(matrix: List[List[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][c] == 0 for c in range(n))
    first_col_zero = any(matrix[r][0] == 0 for r in range(m))
    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0
    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0
    if first_row_zero:
        for c in range(n):
            matrix[0][c] = 0
    if first_col_zero:
        for r in range(m):
            matrix[r][0] = 0
