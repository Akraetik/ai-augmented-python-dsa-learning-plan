# The Method

Why the course is built this way, and how to run it day to day.

## The short version

You don't learn to solve problems by reading solutions. You learn by pulling answers out of your own head,
again and again, with gaps between tries, on problems that are mixed up. That is uncomfortable. It is supposed to be.

## The principles, and where each one lives

| Principle | What it means | Where it shows up |
|---|---|---|
| **Retrieval practice** | Recalling builds memory more than re-reading. | Anki, quizzes, cold solves, audio drills with pauses |
| **Spacing** | Short sessions spread over days beat one long session. | Anki scheduler; the review calendar below |
| **Interleaving** | Mixing problem types teaches you to *pick* the right tool. | Mixed quizzes; later sections pull old problems back in |
| **Worked examples, then fading** | Beginners learn faster from studying a solved example, then a half-solved one, then a blank one. | Lessons → "trace" labs → "fill-in" labs → full labs |
| **Pre-training** | Hearing the key terms before the lesson makes the lesson easier to absorb. | The audio primer comes first in every section |
| **Dual coding** | Words plus a picture beat words alone. | ASCII diagrams in lessons; drawing arrays on paper |
| **Self-explanation** | Explaining *why* a step works locks it in. | `PLAN` block in every lab; the Q&A session |
| **Desirable difficulty** | A little struggle helps memory. Too much stops you. | Hint ladder: three small hints, not one big answer |
| **Mastery learning** | Move on when you can prove it, not when time is up. | The mastery gate at the end of each section |
| **Error-focused practice** | Your own mistakes are the best curriculum. | MISTAKES.md feeds new cards and labs |

## About "learning styles"

The prompt asked for material that fits different learning styles. Here is the honest version.
Studies have not found that matching lessons to a "visual" or "auditory" learner improves results
(Pashler et al., 2008, is the standard review). What *does* help everyone is **variety of format** and
**using the right format for the content.** Code is learned at a keyboard. Vocabulary and pattern triggers
can be learned by ear. Pictures help with pointers and grids.

So this course uses every format. Not to match a style. To give each idea several ways in,
and to fit study into every kind of time you have.

## The section loop

Every section runs the same eight steps.

1. **PRIME — audio primer.** Listen before you open the lesson. Don't take notes. Just get the words in your ear.
2. **LEARN — lessons.** Read with the IDE open. Type every example. Do the trace exercises on paper.
3. **BUILD — labs.** Work in tier order: **Core** (easy), **Build** (medium), **Stretch** (hard), plus one **Bug Hunt**.
4. **DRILL — Anki.** Import the section deck on day one. Do your reviews every day, even on lab-free days.
5. **EXPLAIN — Q&A session.** An oral exam with Claude. You explain; it probes. Instructions are in `qa-session.md`.
6. **TEST — checkpoint quiz.** Open `quiz/quiz.html`. It scores you by topic and names your weak spots.
7. **REPAIR — fix the weak spots.** Log misses in MISTAKES.md. Redo the labs the quiz points to. Add cards.
8. **GATE — prove it.** Two days after your last lab, solve problems from a blank file, timed. Pass the gate, start the next section.

## The problem routine

Use this on every lab until it's automatic. Write steps 1–5 in the `PLAN` comment before you write code.

1. **Restate** the problem in your own words.
2. **Work one example by hand.** On paper. Draw the array.
3. **List edge cases.** Empty. One element. All the same. Negatives. Huge input.
4. **Brute force first.** Say it, and say its Big-O. Don't code it unless you're stuck.
5. **Find the pattern.** Ask: which tool cuts the repeated work?
6. **Code it.**
7. **Test it.** Run your edge cases. Then read your code line by line for the mistakes in MISTAKES.md.

## How to use the hint ladder

Give each problem a real fight first: about 15 minutes of honest effort for Core, 25 for Build, 40 for Stretch.
Then open **one** hint. Try again for 10 minutes before opening the next.

- **Hint 1** asks a question that points you somewhere.
- **Hint 2** names the pattern and the key insight.
- **Hint 3** gives pseudocode.

If you needed Hint 3, mark the problem **"assisted"** in PROGRESS.md. Assisted problems come back as cold solves later.

## Using each kind of time

| Time you have | What to do |
|---|---|
| **Driving, chores (passive)** | Audio tracks. Primer first, then the walk-through tracks, then the rapid-fire drill on repeat. |
| **5–20 minute break** | Anki reviews. If you're caught up, take one quiz section or re-read one hint file. |
| **30–60 minutes at the desk** | One lab, full routine. Or one lesson with all its typing. |
| **2+ hours at the desk** | Lesson → 2–3 labs → review solutions → add cards for anything new. |
| **Before bed** | Anki only. Sleep helps lock it in. |

## The spaced review calendar

The [review/](review/README.md) folder runs this for you each week: `python tools/review.py NN` picks the
cold solves, tapered by age, and the cumulative quiz mixes questions from every past section.
The calendar below is the rule behind it.

Solved problems come back for **cold solves**: blank file, no notes, timer running.

| After you first solve it | Cold solve again |
|---|---|
| +2 days | Gate check |
| +7 days | First review |
| +21 days | Second review |
| +60 days | Long-term check |

Every new section's README lists which old problems are due. If you fail a cold solve, it resets to +2 days.

## Interview reality check (2026)

Big tech still runs live algorithm rounds with AI turned off. Many companies now add a **debug-this-code**
round and expect you to explain your reasoning out loud while you work. That is why every section has a Bug Hunt
lab and a Q&A session. Practice without AI for live rounds. Use AI the way this course does: as a coach, not a crutch.

## Rules that keep this honest

- **Don't read solutions to "learn" a problem.** Solve it, then read the solution to compare.
- **Type, don't paste.** Your fingers need the reps too.
- **Log every repeat mistake.** If it happens twice, it goes in MISTAKES.md and gets a flashcard.
- **No AI during cold solves or gates.** That's the point.
