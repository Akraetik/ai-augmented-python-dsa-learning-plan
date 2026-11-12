"""Images for the Section 04 deck. Run automatically by tools/build_anki.py."""
from card_images import code_image, grid_diagram, grid_row


def build(out):
    grid_diagram([[1, 2, 3], [4, 5, 6]], out / "grid_index.png", highlight={(1, 2)},
                 title="grid[1][2] → 6   (row first, then column)")
    code_image("FOUR  = [(-1, 0), (1, 0), (0, -1), (0, 1)]\nfor dr, dc in FOUR:\n    nr, nc = r + dr, c + dc\n"
               "    if 0 <= nr < rows and 0 <= nc < cols:   # bounds FIRST\n        ...  # grid[nr][nc]",
               out / "code_neighbors.png")
    grid_diagram([[1, 0, 1], [0, "x", 0], [1, 0, 1]], out / "grid_eight.png",
                 highlight={(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)},
                 title="the 8 neighbors of x", show_index=False)
    grid_row([dict(rows=[[1, 2, 3], [4, 5, 6]], title="2 × 3"),
              dict(rows=[[1, 4], [2, 5], [3, 6]], title="3 × 2")], out / "grid_transpose.png", arrows=["transpose"])
    grid_diagram([[1, 2, 3], [4, 5, 6], [7, 8, 9]], out / "grid_diagonals.png",
                 highlight={(0, 0), (1, 1), (2, 2)}, path_cells={(0, 2), (2, 0)},
                 title="main: r == c   ·   anti: r + c == n − 1")
    boxes = [[(r // 3) * 3 + c // 3 for c in range(9)] for r in range(9)]
    grid_diagram(boxes, out / "grid_sudoku_boxes.png", highlight={(4, 7)},
                 title="box = (r // 3) * 3 + c // 3    (4, 7) → 5")
    grid_row([dict(rows=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], title="start"),
              dict(rows=[[1, 4, 7], [2, 5, 8], [3, 6, 9]], title="transpose"),
              dict(rows=[[7, 4, 1], [8, 5, 2], [9, 6, 3]], title="reverse each row")],
             out / "grid_rotate.png", arrows=["flip", "flip"])
    ring = {(0, c) for c in range(4)} | {(r, 3) for r in range(3)} | {(2, c) for c in range(4)} | {(r, 0) for r in range(3)}
    grid_diagram([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], out / "grid_spiral.png", highlight=ring,
                 path_cells={(1, 1), (1, 2)}, title="outer ring first (yellow), then the next ring (blue)")
    code_image("while top <= bottom and left <= right:\n    # top row  → top += 1\n    # right col → right -= 1\n"
               "    if top <= bottom:      # re-check!\n        # bottom row (backward) → bottom -= 1\n"
               "    if left <= right:      # re-check!\n        # left col (upward) → left += 1",
               out / "code_spiral.png")
    grid_row([dict(rows=[[1, 1, 1], [1, 0, 1], [1, 1, 1]], highlight={(1, 1)}, title="find the 0s"),
              dict(rows=[[1, 0, 1], [0, 0, 0], [1, 0, 1]], highlight={(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}, title="then write")],
             out / "grid_set_zeroes.png", arrows=["2nd pass"])
    grid_diagram([[1, "f", "f", "f"], ["f", 5, 6, 7], ["f", 9, 0, 11]], out / "grid_zero_flags.png",
                 highlight={(0, 1), (0, 2), (0, 3), (1, 0), (2, 0)},
                 title="row 0 and column 0 hold the flags (f)")
    code_image("# 0 = dead→dead   1 = live→live\n# 2 = live→dead   3 = dead→live\nwas_live  = value in (1, 2)\n"
               "will_live = value in (1, 3)", out / "code_life_states.png")
