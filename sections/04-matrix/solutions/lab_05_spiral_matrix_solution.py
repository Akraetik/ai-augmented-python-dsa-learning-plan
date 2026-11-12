"""
SOLUTION — Lab 4.05 Spiral Matrix (LeetCode 54)
Time O(m · n). Space O(1) beyond the output.
Four walls. After the top row and right column move two walls, the bottom row and left column
need a re-check: the remaining area may be a single row or column, or empty.
"""
from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    out = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            out.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1):
            out.append(matrix[r][right])
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1):
                out.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):
                out.append(matrix[r][left])
            left += 1
    return out
