"""
SOLUTION — Lab 4.02 Matrix Diagonal Sum (LeetCode 1572)
Time O(n). Space O(1).
One loop over i reads (i, i) and (i, n - 1 - i). When n is odd, the center was added twice: subtract it once.
"""
from typing import List


def diagonal_sum(mat: List[List[int]]) -> int:
    n = len(mat)
    total = 0
    for i in range(n):
        total += mat[i][i] + mat[i][n - 1 - i]
    if n % 2 == 1:
        total -= mat[n // 2][n // 2]
    return total
