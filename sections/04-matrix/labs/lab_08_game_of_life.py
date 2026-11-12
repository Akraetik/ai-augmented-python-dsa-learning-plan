"""
LAB 4.08 — Game of Life                                      Tier: Stretch
LeetCode 289 (Medium) — https://leetcode.com/problems/game-of-life/
Lesson 4.4 · Pattern: extra states (2 = live→dead, 3 = dead→live) so old values survive in place

THE PROBLEM (in our words)
board[r][c] is 1 (live) or 0 (dead). Every cell updates at the same moment from its EIGHT neighbors:
  live, fewer than 2 live neighbors  → dies
  live, 2 or 3                       → lives
  live, more than 3                  → dies
  dead, exactly 3                    → becomes live
Update board in place to the next state. This lab FAILS a full copy of the board.

RETURNS: None. Change board in place.

EXAMPLES
  [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]  ->  [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
  [[1, 1], [1, 0]]                              ->  [[1, 1], [1, 1]]

BEFORE YOU CODE
  Why can't you write the new value straight into each cell?
  With values 0, 1, 2, 3: which ones mean "was live"? Which mean "will be live"?
"""
from typing import List

# PLAN
# RETURNS:
# Why not overwrite directly:
# Was live = values ___; will be live = values ___
# Pass 1 / pass 2:


def game_of_life(board: List[List[int]]) -> None:
    pass


# ---------- tests: don't edit below ----------
import random
import tracemalloc
from _check import check

ENTRY = "game_of_life"
CASES = [
    (([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],), [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]], "glider"),
    (([[1, 1], [1, 0]],), [[1, 1], [1, 1]], "dead cell with 3"),
    (([[1]],), [[0]], "lonely cell dies"),
    (([[0, 0, 0], [1, 1, 1], [0, 0, 0]],), [[0, 1, 0], [0, 1, 0], [0, 1, 0]], "blinker flips"),
    (([[1, 1, 1], [1, 1, 1], [1, 1, 1]],), [[1, 0, 1], [0, 0, 0], [1, 0, 1]], "overcrowded"),
    (([[0, 0], [0, 0]],), [[0, 0], [0, 0]], "all dead"),
]
_r = random.Random(48)
PERF = [("300 x 300", lambda: ([[_r.randint(0, 1) for _ in range(300)] for _ in range(300)],), 3.0)]


def _memory_ok(fn):
    grid = [[(r * 7 + c * 3) % 2 for c in range(500)] for r in range(500)]
    tracemalloc.start()
    fn(grid)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    ok = peak < 200_000
    print(("PASS" if ok else "FAIL") + f" extra memory: {peak / 1000:.0f} KB (limit 200 KB)"
          + ("" if ok else " — that's a copy of the board. Use states 2 and 3 instead."))
    return ok


def run_tests(fn):
    ok = check(fn, CASES, inplace=0, perf=PERF)
    return _memory_ok(fn) and ok if ok else False


if __name__ == "__main__":
    run_tests(game_of_life)
