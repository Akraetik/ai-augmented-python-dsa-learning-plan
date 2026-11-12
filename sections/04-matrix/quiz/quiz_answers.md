# Section 04 · Matrix Checkpoint — Answer Key

**1. A** — Row 0 is [1, 2, 3]. Column 2 of it is 3. *Study: 4.1 Grid Basics › A grid is a list of rows.*

**2. B** — len(grid) counts rows. Each row's length is the number of columns. *Study: 4.1 Grid Basics › A grid is a list of rows.*

**3. B** — Both rows are the same list object. Build rows with a comprehension. *Study: 4.1 Grid Basics › Building a new grid.*

**4. B** — Negative indexes are legal in Python. Always check 0 <= nr < rows first. *Study: 4.1 Grid Basics › Neighbors and the bounds check.*

**5. B** — One visit per cell. That's linear in the grid's size. *Study: 4.1 Grid Basics › Walking every cell.*

**6. B** — (0, n−1), (1, n−2) ... each pair sums to n − 1. *Study: 4.1 Grid Basics › Diagonals.*

**7. B** — (7 // 3) * 3 + 2 // 3 = 2 * 3 + 0 = 6. *Study: 4.2 Rows, Columns, and Boxes › Which box is a cell in?.*

**8. B** — Validity needs every cell. True comes after the loops. (M7) *Study: 4.2 Rows, Columns, and Boxes › Three groups of sets.*

**9. B** — Box (0, 1) and box (1, 0) both give 1. Multiply the box row by 3. *Study: 4.2 Rows, Columns, and Boxes › Common mistakes.*

**10. B** — Two flips make a rotation, like the reversals in lesson 1.3. *Study: 4.3 Rotation and Layers › Rotate 90° clockwise.*

**11. B** — Each pair is swapped twice. Loop only over c > r. *Study: 4.3 Rotation and Layers › Rotate (in-place transpose).*

**12. B** — The top row is done, so the top wall moves down. *Study: 4.3 Rotation and Layers › Spiral order.*

**13. B** — Top row gives 1 2 3 and right moves in. The 'bottom' row is the same row, so it walks back over 2 and 1 again. Re-check top <= bottom first. *Study: 4.3 Rotation and Layers › Spiral order (re-checks).*

**14. B** — Modulo wraps 'up' back to 'right'. *Study: 4.3 Rotation and Layers › Spiral Matrix II (turning walker).*

**15. B** — The scan can't tell new zeros from original ones. Record first, write second. *Study: 4.4 In Place › Set Matrix Zeroes (the trap).*

**16. C** — Mark matrix[r][0] and matrix[0][c]. Save whether row 0 / column 0 had their own zeros first. *Study: 4.4 In Place › Set Matrix Zeroes (the O(1) version).*

**17. B** — Zero them early and every column flag reads as 0. *Study: 4.4 In Place › Set Matrix Zeroes (step 4).*

**18. C** — 2 remembers it WAS live, so neighbors still count it. *Study: 4.4 In Place › Game of Life.*

**19. B** — Reproduction: dead with exactly 3 becomes live. *Study: 4.4 In Place › Game of Life (the rules).*

**20. A** — A mirror is one flip: reverse each row. *Study: Review: review/TRIGGERS.md.*

**21. B** — 180° maps (r, c) to (m−1−r, n−1−c). Compare directly, no copy needed. *Study: Review: review/TRIGGERS.md.*

**22. A** — Each row is just a string. Grid problems often reuse 1D patterns row by row. *Study: Review: review/TRIGGERS.md.*


## If you missed a topic

- **Grid basics (4.1):** Lesson 4.1. Redo labs 01 and 02, and trace the neighbors loop on paper.
- **Rows, columns, boxes (4.2):** Lesson 4.2. Redo lab 03.
- **Rotation and spiral (4.3):** Lesson 4.3. Redo labs 04, 05, 06 and the Bug Hunt (09).
- **In place with markers (4.4):** Lesson 4.4. Redo lab 07 (both versions), then lab 08.
- **Picking the pattern:** Read review/TRIGGERS.md. Cover the right columns and name each pattern.
