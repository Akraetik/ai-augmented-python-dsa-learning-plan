# Section 03 · Sliding Window

**Top Interview 150:** 4 problems (209, 3, 30, 76). **Plus:** Maximum Average Subarray I (643), Permutation in String (567),
Max Consecutive Ones III (1004), Longest Repeating Character Replacement (424), a trace warm-up, and a Bug Hunt.
**What you'll be able to do:** spot a window problem, pick the fixed, longest or shortest template, write it from
memory, and say why it's O(n). Also: know when a window is the wrong tool.
**Pace:** one week.

---

## The three templates

| Lesson | Template | Trigger | Labs |
|---|---|---|---|
| 3.1 | Fixed window: add entering, remove leaving | every window of size k | 01, 02 |
| 3.2 | Longest valid: grow, shrink **while broken**, record **after** | longest run that follows a rule | 03, 04, 05 |
| 3.3 | Shortest valid: grow, **while valid** record **then** shrink | shortest run that meets a goal | 06, 07 |
| 3.4 | Window of word pieces, once per offset | all words, same length, any order | 08 |

## Before you start

1. **Cumulative review** (30–45 min): `review/README.md`. Listen to `review/audio/before-s03.mp3`,
   set the review quiz to "03," and run `python tools/review.py 3`.
2. Import `anki/section-03.apkg`. Daily reviews from today.

## The week

| Day | Do this | Kind of time |
|---|---|---|
| 1 | Cumulative review. Listen: **03-1 Primer**. | drive + break |
| 1 | Lesson 3.1 → labs **01** (Core), **02** (Build) → lab **00** t1, t2 | desk |
| 2 | Listen: **03-2 Walkthrough**. Lesson 3.2 → labs **03, 04** (Build) → lab 00 t3–t5 | drive + desk |
| 3 | Lab **05** (Build). Lab **09** Bug Hunt. | desk |
| 4 | Lesson 3.3 → lab **06** (Build) → lab 00 t6 | desk |
| 5 | Lab **07** (Stretch) → lab 00 t7 | desk |
| 6 | Lesson 3.4 → lab **08** (Stretch) → lab 00 t8. Listen: **03-3 Rapid-Fire Drill** on repeat. | desk + drive |
| 6 | Q&A session (`qa-session.md`). Checkpoint quiz (`quiz/quiz.html`). Repair. | desk + break |
| 8 | Mastery gate (two days after your last lab) | desk |

## Mastery gate

Blank file. No notes, hints, or AI. Timer on.

1. **Quiz:** 85% or better.
2. **Coverage:** lab 01 solved; 4 of 5 Build labs solved without Hint 3; one Stretch lab attempted.
3. **Cold solves:** Longest Substring Without Repeating in **20 minutes**, and Minimum Size Subarray Sum in
   **15 minutes**, talking out loud the whole time.
4. **Explain:** write the longest and shortest templates from memory and name their three differences.

Pass all four: mark Section 03 complete in PROGRESS.md and start Section 04 (Matrix).

## A note on the Bug Hunt

Lab 09 plants a new bug type: shrinking with `if` instead of `while`. If you make it, or find it hard to spot,
add it to `MISTAKES.md` with the check "Is the window valid now, or did I only take one step toward valid?"

## Extra reps (optional)

- LeetCode 239 Sliding Window Maximum (Hard, needs a deque) · 1456 Maximum Number of Vowels in a Substring
- Codility Lesson 15 (Caterpillar Method): CountDistinctSlices, CountTriangles
