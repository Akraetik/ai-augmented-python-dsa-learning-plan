"""
LAB 4.09 — Bug Hunt: Spiral Matrix                           Tier: Bug Hunt
Lesson 4.3 and MISTAKES.md

THE PROBLEM
spiral(matrix) should return every value in spiral order.

  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  ->  [1, 2, 3, 6, 9, 8, 7, 4, 5]
  [[1, 2, 3]]                        ->  [1, 2, 3]

The code uses the four-walls method from lesson 4.3. It has FOUR bugs.
Three match mistakes in MISTAKES.md. One is new: a missing re-check after the walls move.
If you'd make the new one again, add it to MISTAKES.md.

HOW TO DO IT
  1. Don't run it. Trace [[1, 2, 3], [4, 5, 6], [7, 8, 9]], then [[1, 2, 3]], on paper.
  2. List each bug with its line and mistake ID (or "new").
  3. Fix with the smallest changes. Run it. Explain each fix out loud.
"""
from typing import List

# BUGS I FOUND (line, what's wrong, mistake ID or "new")
# 1.
# 2.
# 3.
# 4.


def spiral(matrix: List[List[int]]) -> List[int]:
    out = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for c in range(left, right):
            out.append(matrix[top][c])
        top + 1
        for r in range(top, bottom + 1):
            out.append(matrix[r][right])
        right -= 1
        for c in range(right, left - 1, -1):
            out.append(matrix[bottom][c])
        bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):
                out.append(r)
            left += 1
    return out


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "spiral"
CASES = [
    (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), [1, 2, 3, 6, 9, 8, 7, 4, 5], "3 x 3"),
    (([[1, 2, 3]],), [1, 2, 3], "one row"),
    (([[1], [2], [3]],), [1, 2, 3], "one column"),
    (([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], "3 x 4"),
]
PERF = [("500 x 500", lambda: ([[r * 500 + c for c in range(500)] for r in range(500)],), 1.0)]


def run_tests(fn):
    return check(fn, CASES, perf=PERF)


if __name__ == "__main__":
    run_tests(spiral)
