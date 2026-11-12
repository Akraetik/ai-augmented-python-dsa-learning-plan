# Section 04 · Hint Ladder

One hint at a time. Ten more minutes of effort after each.
Needed Hint 3? Mark the lab **assisted** in PROGRESS.md. It comes back as a cold solve.

---

### 4.01 Transpose Matrix
<details><summary>Hint 1</summary>A 2 × 3 grid turns into what shape? Where does the value at row 0, column 2 end up?</details>
<details><summary>Hint 2</summary>Build an empty cols × rows grid with a comprehension. Then <code>out[c][r] = matrix[r][c]</code>.</details>
<details><summary>Hint 3</summary><code>out = [[0] * rows for _ in range(cols)]</code>, two loops over r and c, return out. Or <code>[list(x) for x in zip(*matrix)]</code>.</details>

### 4.02 Matrix Diagonal Sum
<details><summary>Hint 1</summary>On row i, which column is on the main diagonal? Which on the anti-diagonal?</details>
<details><summary>Hint 2</summary>One loop: add <code>mat[i][i]</code> and <code>mat[i][n − 1 − i]</code>. For odd n, the center was added twice.</details>
<details><summary>Hint 3</summary>After the loop: <code>if n % 2: total −= mat[n // 2][n // 2]</code>.</details>

### 4.03 Valid Sudoku
<details><summary>Hint 1</summary>For each digit, you ask "seen it in this row / column / box?" Which tool answers "seen it?"</details>
<details><summary>Hint 2</summary>27 sets: 9 rows, 9 columns, 9 boxes. Box index <code>(r // 3) * 3 + c // 3</code>. Skip ".".</details>
<details><summary>Hint 3</summary>For each digit: if it's in rows[r], cols[c], or boxes[b] → return False. Else add it to all three. Return True after both loops.</details>

### 4.04 Rotate Image
<details><summary>Hint 1</summary>Lesson 1.3 turned a rotation into reversals. What two flips of a grid make a 90° turn?</details>
<details><summary>Hint 2</summary>Transpose in place (only swap cells with c &gt; r), then reverse each row.</details>
<details><summary>Hint 3</summary>

```
for r in range(n):
    for c in range(r + 1, n):
        m[r][c], m[c][r] = m[c][r], m[r][c]
for row in m: row.reverse()
```
</details>

### 4.05 Spiral Matrix
<details><summary>Hint 1</summary>Walk the outer ring. What four numbers describe the ring you're on?</details>
<details><summary>Hint 2</summary>top, bottom, left, right. Walk top row → top += 1; right column → right −= 1; bottom row → bottom −= 1; left column → left += 1.</details>
<details><summary>Hint 3</summary>Wrap the bottom-row walk in <code>if top &lt;= bottom</code> and the left-column walk in <code>if left &lt;= right</code>. Test a single row and a single column.</details>

### 4.06 Spiral Matrix II
<details><summary>Hint 1</summary>Same path as lab 05. What changes when you write instead of read?</details>
<details><summary>Hint 2</summary>Turning walker: directions right, down, left, up. Turn when the next cell is outside or already filled.</details>
<details><summary>Hint 3</summary>For value 1..n²: write it; compute the next cell; if it's bad, <code>d = (d + 1) % 4</code> and recompute; move.</details>

### 4.07 Set Matrix Zeroes
<details><summary>Hint 1</summary>Trace zeroing a row and column as soon as you see a 0. What happens when the scan reaches the 0s you just wrote?</details>
<details><summary>Hint 2</summary>Two passes: record which rows and columns have a 0, then write. Sets first. For O(1), use row 0 and column 0 as the record.</details>
<details><summary>Hint 3</summary>Save first_row_zero / first_col_zero. Mark <code>m[r][0] = m[0][c] = 0</code> for inner zeros. Zero inner cells by flags. Zero row 0 / column 0 last.</details>

### 4.08 Game of Life
<details><summary>Hint 1</summary>If you write a cell's new state now, what does its neighbor see when it counts?</details>
<details><summary>Hint 2</summary>Use 2 for live→dead and 3 for dead→live. "Was live" means 1 or 2. Second pass: 2 → 0, 3 → 1.</details>
<details><summary>Hint 3</summary>Count neighbors with <code>board[nr][nc] in (1, 2)</code> plus a bounds check. Live with &lt; 2 or &gt; 3 → 2. Dead with 3 → 3.</details>

### 4.09 Bug Hunt
<details><summary>Hint 1</summary>Trace [[1, 2, 3]]. How many times does the 2 get printed? Then trace the 3 × 3: where does the 3 go?</details>
<details><summary>Hint 2</summary>The known bugs are M1, M4, M5. The new one is a missing re-check before the bottom row.</details>
<details><summary>Hint 3</summary><code>range(left, right + 1)</code>. <code>top += 1</code>. Wrap the bottom-row loop in <code>if top &lt;= bottom</code>. Append <code>matrix[r][left]</code>, not <code>r</code>.</details>
