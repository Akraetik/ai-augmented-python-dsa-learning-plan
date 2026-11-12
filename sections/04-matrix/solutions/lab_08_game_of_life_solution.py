"""
SOLUTION — Lab 4.08 Game of Life (LeetCode 289)
Time O(m · n). Space O(1).
States: 0 dead→dead, 1 live→live, 2 live→dead, 3 dead→live.
"Was live" = value in (1, 2). "Will be live" = value in (1, 3).
Pass 1 marks every cell using only the "was live" test. Pass 2 turns 2 → 0 and 3 → 1.
"""
from typing import List

EIGHT = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def game_of_life(board: List[List[int]]) -> None:
    m, n = len(board), len(board[0])
    for r in range(m):
        for c in range(n):
            live = 0
            for dr, dc in EIGHT:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in (1, 2):
                    live += 1
            if board[r][c] == 1 and (live < 2 or live > 3):
                board[r][c] = 2
            elif board[r][c] == 0 and live == 3:
                board[r][c] = 3
    for r in range(m):
        for c in range(n):
            board[r][c] = 1 if board[r][c] in (1, 3) else 0
