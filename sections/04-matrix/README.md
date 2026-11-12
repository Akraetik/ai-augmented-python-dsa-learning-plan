# Section 04 · Matrix

**Top Interview 150:** 5 problems (36, 54, 48, 73, 289). **Plus:** Transpose Matrix (867), Matrix Diagonal Sum (1572),
Spiral Matrix II (59), a trace warm-up, and a Bug Hunt.
**What you'll be able to do:** move around a grid without index bugs, rotate and spiral it, and change it in place
without losing the information you still need.
**Pace:** one week.

---

## The four ideas

| Lesson | Idea | Trigger | Labs |
|---|---|---|---|
| 4.1 | Grid basics: `grid[r][c]`, neighbors, bounds, transpose, diagonals | any 2D grid | 01, 02 |
| 4.2 | One set per row / column / box | "no repeats in each group" | 03 |
| 4.3 | Rotate = transpose + reverse; spiral = four shrinking walls | rotate, spiral order | 04, 05, 06 |
| 4.4 | Record first, write second, using spare cells or extra states | in-place updates that depend on the original | 07, 08 |

## Before you start

1. **Cumulative review** (30–45 min): `review/README.md`. Listen to `review/audio/before-s04.mp3`,
   set the review quiz to "04," and run `python tools/review.py 4`.
2. Import `anki/section-04.apkg`. Daily reviews from today.

## The week

| Day | Do this | Kind of time |
|---|---|---|
| 1 | Cumulative review. Listen: **04-1 Primer**. | drive + break |
| 1 | Lesson 4.1 → labs **01, 02** (Core) → lab **00** t1–t3, t8 | desk |
| 2 | Lesson 4.2 → lab **03** (Build) → lab 00 t4 | desk |
| 3 | Listen: **04-2 Walkthrough**. Lesson 4.3 → labs **04, 05, 06** (Build) → lab 00 t5, t6 | drive + desk |
| 4 | Lab **09** Bug Hunt | desk |
| 5 | Lesson 4.4 → lab **07** (Build, both versions) → lab 00 t7 | desk |
| 6 | Lab **08** (Stretch). Listen: **04-3 Rapid-Fire Drill** on repeat. | desk + drive |
| 6 | Q&A session (`qa-session.md`). Checkpoint quiz (`quiz/quiz.html`). Repair. | desk + break |
| 8 | Mastery gate (two days after your last lab) | desk |

## Mastery gate

Blank file. No notes, hints, or AI. Timer on.

1. **Quiz:** 85% or better.
2. **Coverage:** both Core labs; 4 of 5 Build labs without Hint 3; Game of Life attempted.
3. **Cold solves:** Rotate Image in **15 minutes**, and Spiral Matrix in **20 minutes**, talking out loud.
   Test a single row and a single column before you say "done."
4. **Explain:** Set Matrix Zeroes in O(1) space, all four steps, in under two minutes.

Pass all four: mark Section 04 complete in PROGRESS.md and start Section 05 (Hashmap).

## A note on the Bug Hunt

Lab 09 plants a new bug type: a missing re-check after the walls move. If you make it, add it to
`MISTAKES.md` with the check "After moving walls, is there still a row or column left to walk?"

## Extra reps (optional)

- LeetCode 240 Search a 2D Matrix II · 1582 Special Positions in a Binary Matrix · 1886 Determine Whether Matrix Can Be Obtained By Rotation
