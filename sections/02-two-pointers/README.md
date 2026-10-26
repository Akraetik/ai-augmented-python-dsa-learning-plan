# Section 02 · Two Pointers

**Top Interview 150:** 5 problems (125, 392, 167, 11, 15). **Plus:** Squares of a Sorted Array (977), 3Sum Closest (16),
Trapping Rain Water again in O(1) space (42), a trace warm-up, and a Bug Hunt.
**What you'll be able to do:** pick the right two-pointer shape, move the right pointer, and say in one sentence
*why* that move is safe. That sentence is what interviewers listen for.
**Pace:** one week.

---

## The four shapes

| Lesson | Shape | Trigger | Labs |
|---|---|---|---|
| 2.1 | Opposite ends, walk inward | sorted + pair; symmetry | 01, 03, 04 |
| 2.2 | Same direction, fast and slow | "in order" across two sequences | 02 |
| 2.3 | Shrink the weaker side | maximize something capped by the smaller side | 05 |
| 2.4 | Sort, fix one, two-pointer the rest | "k numbers that sum to X" | 06, 08 |
| 2.5 | Two pointers instead of prefix/suffix lists | same answer, O(1) space | 07 |

## Before you start

1. **Cumulative review** (30–45 min): `review/README.md`. Listen to `review/audio/before-s02.mp3`,
   set the review quiz to "02," and run `python tools/review.py 2`.
2. Import `anki/section-02.apkg`. Daily reviews from today.

## The week

| Day | Do this | Kind of time |
|---|---|---|
| 1 | Cumulative review. Listen: **02-1 Primer**. | drive + break |
| 1–2 | Lesson 2.1 → labs **01, 04** (Core), **03** (Build) → lab **00** t1, t3, t4 | desk |
| 2 | Lesson 2.2 → lab **02** (Core) → lab 00 t2 | desk |
| 3 | Listen: **02-2 Walkthrough**. Lesson 2.3 → lab **05** (Build) → lab 00 t5, t6 | drive + desk |
| 4 | Lesson 2.4 → labs **06, 08** (Build) → lab 00 t7, t8 | desk |
| 4 | Lab **09** Bug Hunt | desk |
| 5 | Lesson 2.5 → lab **07** (Stretch) | desk |
| 5–6 | Listen: **02-3 Rapid-Fire Drill** on repeat. Q&A session (`qa-session.md`). | drive + desk |
| 6 | Checkpoint quiz (`quiz/quiz.html`). Repair using the study list. | break + desk |
| 8 | Mastery gate (two days after your last lab) | desk |

## Mastery gate

Blank file. No notes, hints, or AI. Timer on.

1. **Quiz:** 85% or better.
2. **Coverage:** every Core lab solved; 3 of 4 Build labs solved without Hint 3.
3. **Cold solves:** Two Sum II in **15 minutes**, and either Container or 3Sum in **25 minutes**,
   talking out loud the whole time.
4. **Explain:** for each of the five shapes, the trigger and the one-sentence "why that pointer moves."

Pass all four: mark Section 02 complete in PROGRESS.md and start Section 03 (Sliding Window).

## A note on the Bug Hunt

Lab 09 has a bug type that isn't in `MISTAKES.md` yet: moving the wrong pointer. If you make it, or find
it hard to spot, add it as **M8** with the check "Which pointer moves the sum the way I need?"

## Extra reps (optional)

- LeetCode 680 Valid Palindrome II · 88 Merge Sorted Array (revisit: same-direction pointers from the back)
- Codility Lesson 15 (Caterpillar Method): AbsDistinct, CountDistinctSlices
