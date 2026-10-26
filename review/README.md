# Cumulative Review

Do this at the **start of every new section**, before its audio primer. It covers **every** section you've
finished. The newest section gets the most time. Older ones taper off but never drop to zero, so nothing fades.

**Time:** 30–45 minutes. **Rule:** no notes, no hints, no AI during the quiz and cold solves.

## The routine

| # | Step | Where | Time | Kind of time |
|---|---|---|---|---|
| 1 | Listen to the review track for the section you're starting | `audio/before-sNN.mp3` | 5–8 min | drive |
| 2 | Read the triggers table. Cover the right columns and name each pattern. | `TRIGGERS.md` | 5 min | break |
| 3 | Read the newest review sheet in full. Skim older sheets' tables only. | `sheets/` | 5–10 min | break |
| 4 | Take the cumulative quiz. Pick the section you're starting. | `quiz.html` | 10 min | break |
| 5 | Pick and do this week's cold solves | `python tools/review.py NN` | 20–60 min | desk |
| 6 | Log your quiz score and anything you missed | `REVIEW-LOG.md` | 2 min | any |

Missed something? The quiz and labs print exactly which lesson section to restudy. Fix it before you start
the new section's lessons. If the same thing is missed twice, it goes in `MISTAKES.md` and gets a card.

## The taper

How much of each past section you see, by how many sections ago you finished it:

| Sections ago | Quiz questions | Audio questions | Cold solves |
|---|---|---|---|
| 1 (just finished) | 10 | 30 | 2 |
| 2 | 6 | 18 | 1 |
| 3 | 4 | 12 | 1 every other week |
| 4 or more | 3 each | 8 each | 1 every other week, rotating |

The quiz also gives extra weight to questions you missed last time, and less to ones you got right.
Your quiz history is saved in your browser.

## What already tapers on its own

**Anki.** Keep every section's deck inside the one parent deck, `DSA Mastery`, and study the parent.
Anki's scheduler already spaces old cards further and further apart, so older sections take fewer minutes
each week without you doing anything. The review here adds the parts Anki can't do: mixed problem solving,
timed cold solves, and pattern recognition across sections.

## Files

| File | What it is |
|---|---|
| `TRIGGERS.md` | Every pattern trigger in the course, one table. Grows each section. |
| `sheets/NN-name.md` | One-page summary per section: patterns, skeletons, traps. |
| `quiz.html` | Cumulative quiz. Pick the section you're starting; it builds a tapered mixed set. |
| `audio/before-sNN.mp3` | Rapid-fire review track for the week you start section NN, tapered. |
| `cold-solves/` | Blank problem files `tools/review.py` copies here each week. |
| `REVIEW-LOG.md` | Your weekly log: date, cold solves, quiz score. Created on first use. |

## Rebuilding after a new section

```
python tools/build_review.py      # rebuilds quiz.html and the audio scripts from every section
python tools/build_audio.py review
```

Then add the new section's rows to `TRIGGERS.md` and write its sheet in `sheets/`.
