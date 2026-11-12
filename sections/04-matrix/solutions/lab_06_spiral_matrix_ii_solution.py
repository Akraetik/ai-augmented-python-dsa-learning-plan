"""
SOLUTION — Lab 4.06 Spiral Matrix II (LeetCode 59)
Time O(n²). Space O(n²) for the output.
Turning walker: move in direction d; if the next cell is outside or already filled, turn right with
d = (d + 1) % 4. (Four walls, like lab 05, works too.)
"""
from typing import List

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]   # right, down, left, up


def generate_matrix(n: int) -> List[List[int]]:
    grid = [[0] * n for _ in range(n)]
    r = c = d = 0
    for value in range(1, n * n + 1):
        grid[r][c] = value
        dr, dc = DIRS[d]
        nr, nc = r + dr, c + dc
        if not (0 <= nr < n and 0 <= nc < n) or grid[nr][nc] != 0:
            d = (d + 1) % 4
            dr, dc = DIRS[d]
            nr, nc = r + dr, c + dc
        r, c = nr, nc
    return grid
