# Section 00 · Foundations: Python for Interviews + Big-O

**What you'll be able to do:** read and write the Python that interview problems use, judge how fast code is
before running it, and follow a routine when you're stuck.

**Estimated effort:** 6–12 hours of desk time, plus audio and Anki. Faster if you pass the diagnostic.

---

## Step 0 — Take the diagnostic (15 min)

Open `quiz/quiz.html` in a browser. No notes, no IDE, no AI.

- **85% or better:** fast track. Skim the lessons for your weak topics only. Do labs 05, 09, 10, and 11.
  Import the Anki deck. Then go to Section 01.
- **Below 85%:** take the full path below. Retake the quiz at the end.

## The full path

Check each box in PROGRESS.md as you go.

| # | Do this | Where | Time | Kind of time |
|---|---|---|---|---|
| 1 | Import the deck. Start daily reviews. | `anki/section-00.apkg` | 5 min | any |
| 2 | Listen: **00-1 How This Works** | `audio/` | 7 min | drive |
| 3 | Read lesson 00.1 | `lessons/00.1-how-coding-tests-work.md` | 20 min | desk |
| 4 | Listen: **00-2 Big-O by Ear** | `audio/` | 9 min | drive |
| 5 | Read lesson 00.2. Do `lab_01_bigo_spotter.py` | lessons, labs | 60 min | desk |
| 6 | Listen: **00-3 The Python Toolkit** | `audio/` | 10 min | drive |
| 7 | Read lessons 00.3 and 00.4. Type every example. | lessons | 2 hrs | desk |
| 8 | Do `lab_00_trace_basics.py` | labs | 30 min | desk |
| 9 | Do labs 02, 03, 04 | labs | 1 hr | desk |
| 10 | Read lesson 00.5 | lessons | 30 min | desk |
| 11 | Do labs 05–09 (Core) | labs | 2 hrs | desk |
| 12 | Do lab 10 (Speed Trap) and lab 11 (Bug Hunt) | labs | 1 hr | desk |
| 13 | Listen: **00-4 Rapid-Fire Drill** (repeat it) | `audio/` | 7 min | drive |
| 14 | Q&A session with Claude | `qa-session.md` | 20 min | desk |
| 15 | Checkpoint quiz (same quiz, retake) | `quiz/quiz.html` | 15 min | break |
| 16 | Gate (below) | blank file | 45 min | desk |

## Mastery gate

Wait at least **one day** after your last lab. Then, in a blank file, no notes, no AI:

1. Solve **Two Sum** in under 15 minutes.
2. Solve **Max Consecutive Ones** in under 10 minutes.
3. For three snippets from `lab_01_bigo_spotter.py`, say the Big-O out loud and why, in under a minute each.
4. Quiz score **85%+**.

All four done? Mark Section 00 complete in PROGRESS.md. Start Section 01.
Missed one? Redo that lab tomorrow and try the gate again in two days.

## What you can skip if you already know it

| If you can already... | Skip |
|---|---|
| write a function that returns a value and explain `self` | lesson 00.1 |
| explain why `x in list` is slow and `x in set` is fast | lesson 00.2 (still do lab 01) |
| use `enumerate`, slicing, `split`, `join` without looking | lesson 00.3 |
| use `Counter`, `defaultdict`, `deque`, `sorted(key=...)` | lesson 00.4 |
