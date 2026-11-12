# Iterations

Changes to the course itself: what you asked for, what changed, and where it applies.
Add a row whenever testing a section shows something to improve. Each new section is built to the latest
standards listed here.

**Status:** `done` · `in progress` · `planned` · `rejected` (with a reason)

## Log

| # | Date | Request / finding | Change made | Applies to | Status |
|---|---|---|---|---|---|
| 1 | 2026-10-25 | Course built from PROMPT.md | Sections 00 and 01. Labs with tests, hint ladders, solutions, Anki, audio, quizzes, Q&A, gates. | 00, 01 | done |
| 2 | 2026-10-25 | Testing Section 00: card length is right. | No change. Keep the current card density as the standard. | all | done |
| 3 | 2026-10-25 | Testing Section 00: Big-O cards are hard to understand without context. Add images of code or graphics. | `build_anki.py` now embeds images. `tools/card_images.py` draws code snippets, Big-O growth charts, array diagrams with pointers, grids, tables, and before/after pictures. Piloted on the 18 Big-O cards in Section 00 (16 images). | 00 (pilot), 02+ by default | done |
| 4 | 2026-10-25 | After lab 00 trace basics: each wrong answer should say what subject it was and where to study it. | Every miss now prints a study pointer. Trace/Big-O labs: lesson file + section per question. Code labs: lesson file, pattern, hint, mistake log on any failure (and the hidden-loops table when only speed fails). Quizzes: per-question "If you missed it, study" line, plus a numbered study list in the results and in "Copy results for Claude." | 00, 01, all future | done |
| 5 | 2026-10-25 | Wanted a graphical flow chart of what to do first. | `docs/study-flow.png` (Mermaid source `docs/study-flow.mmd`), shown at the top of README. | all | done |
| 6 | 2026-10-25 | Wanted a spaced-repetition review of all previous sections that grows each section, with less review on older ones. Pace: about one section per week. | New `review/` folder: tapered review audio per section, `TRIGGERS.md` (all triggers, grows each section), one-page sheets, a cumulative quiz that tapers by section age and re-weights past misses, and `tools/review.py` for tapered cold solves. README pace note: one section per week (Section 01 two to three). | 01+ | done |
| 7 | 2026-10-25 | Asked for the next section. | Section 02 Two Pointers built to all current standards: 5 lessons, 10 labs (5 Top-150 + 977, 16, 42-in-O(1), trace, Bug Hunt), hints, solutions, 33 cards with 11 images, 22-question quiz with study pointers, Q&A, 3 audio tracks. Review folder grew: sheet 02, 7 trigger rows, `before-s03` track. Runner now stops an infinite loop after 5 s and says why. Lab 07 measures extra memory. Bug Hunt introduces candidate M8 (moving the wrong pointer). | 02, runner for all | done |
| 8 | 2026-10-26 | Created the GitHub repo as `Akraetik/ai-augmented-python-dsa-learning-plan`. Keep that name. | Renamed everywhere: README title and repo link, PROMPT.md, Q&A prompts, GitHub guide (push URL, folder name, rejected-push fix), audio intro 00-1 re-rendered, all MP3s retagged. Anki parent deck stays "DSA Mastery" so re-imports update cards instead of duplicating them. Delivered Sections 00–02 as one complete zip for the first push. | all | done |
| 9 | 2026-10-26 | Decided the repo stays public, mistake log included: "I am learning and growing along the way." | No change to files. Logs stay public by design. | all | done |
| 10 | 2026-11-11 | Asked for Section 03. | Section 03 Sliding Window built to all current standards: 4 lessons, 10 labs (4 Top-150 + 643, 567, 1004, 424, trace, Bug Hunt), hints, solutions, 29 cards with 8 images, 22-question quiz with study pointers, Q&A, 3 audio tracks. Solutions checked against brute force on 5,000 random inputs; all 8 slow approaches fail the speed tests. Review folder grew: sheet 03, 8 trigger rows, `before-s04` track. Bug Hunt introduces candidate M9 (shrinking with `if` instead of `while`). Delivered as an update zip that leaves PROGRESS.md and MISTAKES.md untouched. | 03 | done |
| 11 | 2026-11-11 | Asked for Section 04. | Section 04 Matrix built to all current standards: 4 lessons, 10 labs (5 Top-150 + 867, 1572, 59, trace, Bug Hunt), hints, solutions, 29 cards with 12 grid images (new side-by-side grid helper), 22-question quiz with study pointers, Q&A, 3 audio tracks. Solutions checked against reference versions on 3,000 random grids. Memory checks fail full copies in Rotate Image, Set Matrix Zeroes, and Game of Life; Set Matrix Zeroes also reports whether the O(1) follow-up was reached. Review folder grew: sheet 04, 6 trigger rows, `before-s05` track. Bug Hunt introduces candidate M10 (missing re-check after walls move). | 04 | done |

## Feedback so far

What you've said while testing, in your words where possible. This is what the standards below are built on.

| Date | Where | Verdict | What you said | What changed |
|---|---|---|---|---|
| 2026-10-25 | Section 00 overall | 👍 good | "It seems good." | Kept the structure for every section. |
| 2026-10-25 | Anki, Section 00 | 👍 good | Cards are the correct length. | Card density locked in as the standard (#2). |
| 2026-10-25 | Audio 00-1 | 👍 good | "It explains everything on 00-1." | Every section keeps a primer track first. |
| 2026-10-25 | Anki, Big-O cards | 👎 needs work | Hard to understand without context; wanted code images or graphics. | Card images (#3). |
| 2026-10-25 | Lab 00 trace basics | 👎 needs work | Wanted to know the subject and where to study after a wrong answer. | Study pointers on every miss (#4). |
| 2026-10-25 | Overall flow | 👎 unclear | Wanted a flow chart of what to do first. | Study-flow chart (#5). |
| 2026-10-25 | Retention | ➕ request | A review of all older sections that grows each section, with less on older ones. One section per week. | Cumulative, tapered `review/` folder (#6). |
| 2026-10-26 | Repo name | ➕ decision | Named the repo `ai-augmented-python-dsa-learning-plan`. | Rename (#8). |
| 2026-10-26 | Public repo | 👍 decision | "I am okay with my mistakes being known. I am learning and growing along the way." | Repo and mistake log stay public (#9). |

## Current standards for new sections

These come from the log above. Check each one when building a section.

**Anki cards**
- Same density as Section 00: one idea per card, short back, at most about five bullets.
- Add an image where a picture explains faster than words:
  - **Big-O / growth:** a growth chart with the relevant curve highlighted.
  - **Pointers and indexes:** an array diagram with labeled arrows (`left`, `right`, `read`, `write`).
  - **Code patterns and skeletons:** a highlighted code image, with comments carrying the reasoning.
  - **Grids, matrices, DP tables:** a grid diagram with the filled or visited cells highlighted.
  - **Before/after operations:** stacked before and after diagrams.
  - **Trees, graphs, linked lists:** node-and-edge diagrams (helper to be added in Section 08).
- Add a one-line "why" or context sentence next to each image, not just the bare answer.

**Every miss**
- Every quiz question has a `study=` pointer (lesson › section). Every trace lab has a `STUDY` map.
- Code lab docstrings keep the `Lesson X.Y · Pattern: ...` line; the runner reads it.

**Labs**
- Every section has a trace warm-up, Core/Build/Stretch labs, and a Bug Hunt.
- Speed tests must fail the brute-force approach (check it with a slow version before shipping).
- Where the lesson promises O(1) space, the lab measures memory.
- Grid problems are naturally O(m · n), so brute force often isn't slower. Speed tests target the real
  slow habits (scanning every cell to find a diagonal, re-scanning rows and columns per cell); memory tests
  catch full copies.

**Review**
- Each new section adds its rows to `review/TRIGGERS.md`, a one-page `review/sheets/NN-name.md`,
  and a rapid-fire audio script (the review track samples from it). Then rerun `tools/build_review.py`.

## How to add an iteration

1. Add a row to the log: the date, what you noticed (in your words), and `planned`.
2. Ask Claude to make the change, or make it yourself.
3. Fill in "Change made" and "Applies to." Set status to `done`.
4. If it changes how future sections are built, add it to **Current standards**.

## Backlog

Ideas not yet scheduled.

| Idea | Notes |
|---|---|
| | |
