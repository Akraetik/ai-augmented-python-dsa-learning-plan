# Section 04 · Matrix Checkpoint

22 questions · pass mark 85% · no notes, no IDE, no AI. Answers: [quiz_answers.md](quiz_answers.md). Better: open `quiz.html` in a browser for instant scoring by topic.

**1.** *(Grid basics (4.1))* grid = [[1, 2, 3], [4, 5, 6]]. What is `grid[0][2]`?

- A. 3
- B. 4
- C. 2
- D. IndexError

**2.** *(Grid basics (4.1))* How do you get the number of columns?

- A. len(grid)
- B. len(grid[0])
- C. grid.cols
- D. len(grid) * len(grid[0])

**3.** *(Grid basics (4.1))* `g = [[0] * 3] * 2`, then `g[0][0] = 9`. What is `g`?

- A. [[9, 0, 0], [0, 0, 0]]
- B. [[9, 0, 0], [9, 0, 0]]
- C. [[9, 9, 9], [0, 0, 0]]
- D. Error

**4.** *(Grid basics (4.1))* You skip the bounds check and read `grid[-1][c]` for a cell in row 0. What happens?

- A. IndexError
- B. It reads the last row: a silent wrong answer
- C. It returns None
- D. It reads row 1

**5.** *(Grid basics (4.1))* Big-O of visiting every cell of an m × n grid once?

- A. O(m + n)
- B. O(m · n)
- C. O((m · n)²)
- D. O(log m)

**6.** *(Grid basics (4.1))* n × n grid. Which cells are on the anti-diagonal?

- A. r == c
- B. r + c == n − 1
- C. r − c == 1
- D. r + c == n

**7.** *(Rows, columns, boxes (4.2))* Sudoku box index for cell (7, 2)?

- A. 2
- B. 6
- C. 7
- D. 9

**8.** *(Rows, columns, boxes (4.2))* Valid Sudoku: when can you return True?

- A. After the first valid row
- B. After every cell is checked
- C. When a box is full
- D. After 9 digits

**9.** *(Rows, columns, boxes (4.2))* Why is `r // 3 + c // 3` a wrong box index?

- A. It's too slow
- B. It only gives 0–4, so different boxes collide
- C. It's off by one
- D. It ignores "."

**10.** *(Rotation and spiral (4.3))* Rotate an n × n grid 90° clockwise in place. Steps?

- A. Reverse each row, then transpose
- B. Transpose, then reverse each row
- C. Transpose twice
- D. Reverse the rows, then reverse each row

**11.** *(Rotation and spiral (4.3))* In-place transpose swaps every (r, c) with (c, r) for ALL r and c. Result?

- A. Correct transpose
- B. The grid ends up unchanged
- C. IndexError
- D. Half transposed

**12.** *(Rotation and spiral (4.3))* Spiral Matrix: after walking the top row, which wall moves?

- A. bottom −= 1
- B. top += 1
- C. left += 1
- D. right −= 1

**13.** *(Rotation and spiral (4.3))* Spiral on `[[1, 2, 3]]` with no re-check before the bottom row. Output?

- A. [1, 2, 3]
- B. [1, 2, 3, 2, 1]
- C. [3, 2, 1]
- D. []

**14.** *(Rotation and spiral (4.3))* Turning walker with directions right, down, left, up. How do you turn right?

- A. d += 1
- B. d = (d + 1) % 4
- C. d = -d
- D. d = (d − 1) % 4

**15.** *(In place with markers (4.4))* Set Matrix Zeroes: why not zero the row and column the moment you see a 0?

- A. It's too slow
- B. The new zeros trigger more zeroing
- C. Python forbids it
- D. It uses too much memory

**16.** *(In place with markers (4.4))* O(1) Set Matrix Zeroes stores its flags where?

- A. A set
- B. A copy of the grid
- C. Row 0 and column 0 of the grid
- D. A dictionary

**17.** *(In place with markers (4.4))* O(1) Set Matrix Zeroes: why zero row 0 and column 0 LAST?

- A. They're the biggest
- B. They hold flags the inner cells still need
- C. Tradition
- D. To save time

**18.** *(In place with markers (4.4))* Game of Life in place: a cell holds 2. What does it mean?

- A. Dead → dead
- B. Live → live
- C. Live now, dead next
- D. Dead now, live next

**19.** *(In place with markers (4.4))* A dead cell has exactly 3 live neighbors. Next state?

- A. Dead
- B. Live

**20.** *(Picking the pattern)* "Flip the image horizontally (mirror each row)." Simplest tool?

- A. Reverse each row
- B. Transpose
- C. Spiral walk
- D. Sets per row

**21.** *(Picking the pattern)* "Is this grid the same after a 180° turn?" Fastest check?

- A. Rotate twice and compare
- B. Compare grid[r][c] with grid[m−1−r][n−1−c] for every cell
- C. Spiral order
- D. Sudoku sets

**22.** *(Picking the pattern)* "Longest row-substring with no repeated letters." Which earlier pattern applies to each row?

- A. Sliding window, longest valid (Section 03)
- B. Two pointers from the ends
- C. Transpose
- D. Prefix sums

