"""
SOLUTION — Lab 4.09 Bug Hunt: Spiral Matrix

The four bugs:
1. range(left, right) skips the last column of the top row.   -> M5. Fix: range(left, right + 1)
2. top + 1 is never saved.                                     -> M4. Fix: top += 1
3. The bottom row runs with no re-check.                       -> NEW: missing re-check after walls move.
   On [[1, 2, 3]] the top row is gone, but the bottom row prints it again backward.
   Fix: wrap the bottom-row loop in `if top <= bottom:`.
   Check: "After moving walls, is there still a row (or column) left to walk?"  Candidate M10.
4. out.append(r) adds the row number, not the value.          -> M1. Fix: out.append(matrix[r][left])
"""
from typing import List


def spiral(matrix: List[List[int]]) -> List[int]:
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
