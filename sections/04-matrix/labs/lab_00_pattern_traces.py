"""
LAB 4.00 — Pattern Traces                                    Tier: Warm-up
Do each question right after its lesson. Trace on paper, write the result as a Python value, run the file.
It says which you got right, not what the answers are. Each miss prints where to study.
Answers with explanations: solutions/lab_00_pattern_traces_answers.md
"""

# t1 (Lesson 4.1)
# grid = [[1, 2, 3], [4, 5, 6]]. What is grid[1][2]?

# t2 (Lesson 4.1)
# Same grid. Write [number of rows, number of columns].

# t3 (Lesson 4.1)
# Transpose of [[1, 2, 3], [4, 5, 6]]?

# t4 (Lesson 4.2)
# Valid Sudoku box numbers run 0-8, left to right, top to bottom.
# Which box is cell (r=4, c=7) in?

# t5 (Lesson 4.3)
# Rotate [[1, 2], [3, 4]] 90 degrees clockwise.

# t6 (Lesson 4.3)
# Spiral order of [[1, 2, 3], [4, 5, 6], [7, 8, 9]]?

# t7 (Lesson 4.4)
# Set Matrix Zeroes on [[1, 1, 1], [1, 0, 1], [1, 1, 1]]. The result?

# t8 (Lesson 4.4)
# Game of Life board [[1, 1, 0], [0, 1, 0], [1, 0, 1]].
# How many LIVE neighbors does the center cell (1, 1) have? (Count all eight around it.)


ANSWERS = {
    "t1": ...,
    "t2": ...,
    "t3": ...,
    "t4": ...,
    "t5": ...,
    "t6": ...,
    "t7": ...,
    "t8": ...,
}

# ---------- tests: don't edit below ----------
from _check import check_answers

KEY = {'t1': 'a7ecf09846430c50', 't2': 'f8916fc97f4963ce', 't3': '6d4d316b2b57c382', 't4': '2567637a88a909ac', 't5': 'fba30abd4150f548', 't6': 'daea1a20ba8233f6', 't7': '3096eeff47a1c0a3', 't8': '55b9d8d4fca4992b'}
STUDY = {
    't1': 'lessons/4.1-grid-basics.md › A grid is a list of rows (row first, then column)',
    't2': 'lessons/4.1-grid-basics.md › A grid is a list of rows (len(grid), len(grid[0]))',
    't3': 'lessons/4.1-grid-basics.md › Transpose',
    't4': 'lessons/4.2-boxes-and-lookups.md › Which box is a cell in?',
    't5': 'lessons/4.3-rotation-and-layers.md › Rotate 90° clockwise (transpose, then reverse each row)',
    't6': 'lessons/4.3-rotation-and-layers.md › Spiral order (four walls)',
    't7': 'lessons/4.4-in-place-with-markers.md › Set Matrix Zeroes (record first, write second)',
    't8': 'lessons/4.1-grid-basics.md › Neighbors and the bounds check (eight directions)',
}
ENTRY = "ANSWERS"


def run_tests(answers):
    return check_answers(answers, KEY, title="pattern traces", study=STUDY)


if __name__ == "__main__":
    run_tests(ANSWERS)
