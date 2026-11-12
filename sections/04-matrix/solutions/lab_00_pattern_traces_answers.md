# Lab 4.00 — Pattern Traces: Answers

| Q | Answer | Why |
|---|---|---|
| t1 | `6` | Row 1 is `[4, 5, 6]`. Column 2 of it is 6. Row first, then column. |
| t2 | `[2, 3]` | `len(grid)` is 2 rows. `len(grid[0])` is 3 columns. |
| t3 | `[[1, 4], [2, 5], [3, 6]]` | Row r, column c moves to row c, column r. 2 × 3 becomes 3 × 2. |
| t4 | `5` | `(4 // 3) * 3 + (7 // 3)` = `1 * 3 + 2`. |
| t5 | `[[3, 1], [4, 2]]` | Transpose → `[[1, 3], [2, 4]]`, then reverse each row. |
| t6 | `[1, 2, 3, 6, 9, 8, 7, 4, 5]` | Top, right, bottom (backward), left (upward), then the center. |
| t7 | `[[1, 0, 1], [0, 0, 0], [1, 0, 1]]` | Only row 1 and column 1 hold the original 0. |
| t8 | `4` | (0,0), (0,1), (2,0), (2,2) are live. The center itself doesn't count. |
