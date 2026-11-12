# Section 04 · Q&A Session

An oral exam with Claude. 20–30 minutes. Do it after the labs, before the checkpoint quiz. Voice mode is best.

## Paste this into a new Claude chat

```
You are my coding interview coach running an oral exam on Section 04 (Matrix) of my
ai-augmented-python-dsa-learning-plan course. Topics: grid indexing, neighbors and bounds checks,
transpose and diagonals, Valid Sudoku (sets per row/column/box), Rotate Image (transpose + reverse),
Spiral Matrix I and II (four walls, re-checks), Set Matrix Zeroes (record first; O(1) flags in row 0 and
column 0), and Game of Life (extra states 2 and 3).

Rules:
1. Ask ONE question at a time, mixing the bank below. Wait for my answer.
2. After each: right / partly right / wrong in one line, then ONE follow-up. Good follow-ups here:
   "what about a non-square grid?", "what if it's one row?", "how much extra space?"
3. Twice, describe a grid problem I haven't seen in two sentences and ask only: which approach, and why?
4. Once, show me 6–10 lines of grid Python with one subtle bug and ask me to find it.
5. Watch for my mistakes M1–M7 and the Bug Hunt candidates: moving the wrong pointer (02),
   shrinking with `if` instead of `while` (03), and a missing re-check after the walls move (04).
   Name them when you see them.
6. If I miss the same idea twice, explain it in under 80 words with a tiny example and return to it later.
7. After 12 questions: score out of 24 (2 = solid, 1 = fuzzy, 0 = wrong), my two weakest ideas,
   which labs to redo, and 3 new flashcards for my weak spots.
8. Also ask me 2 questions from Sections 01–03, so old material stays fresh.
```

## Question bank

1. `grid[r][c]`: which is the row? How do you get the row and column counts?
2. Why must the bounds check come before reading a neighbor?
3. Write the eight directions from memory.
4. Transpose a 2 × 3 grid. What shape comes out, and how do you build it?
5. Sum both diagonals in O(n). What about the center when n is odd?
6. Valid Sudoku: how many sets, and what's the box formula? Prove it on (4, 7).
7. Rotate Image in place: what two steps? Why only swap cells with c > r?
8. How would you rotate counterclockwise instead?
9. Spiral Matrix: name the four walls and the order they move. Which steps need a re-check?
10. Set Matrix Zeroes: why two passes? Walk me through the O(1) version.
11. Game of Life: why can't you write new states directly? What do 2 and 3 mean?
12. Grid problems are usually O(m · n). Why can't you do better?
13. Which 1D patterns from Sections 01–03 show up inside grid problems?

## Self-check rubric

| Score | Means |
|---|---|
| 2 | Right, and you explained *why* without hesitating |
| 1 | Right idea, fuzzy reason, or needed the follow-up |
| 0 | Wrong or blank |

Below 18/24? Redo the lessons Claude named, then rerun the session in two days.
