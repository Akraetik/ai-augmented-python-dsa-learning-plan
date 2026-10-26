# Section 01 · Array / String

**Top Interview 150:** 24 problems. **Plus:** a pattern-trace warm-up and a Bug Hunt.
**What you'll be able to do:** recognize the seven array/string patterns on sight, pick the right one, and code it
in O(n) under time pressure.
**Estimated effort:** 25–40 hours of desk time over 2–4 weeks, plus daily Anki and audio.

---

## The seven patterns in this section

| Lesson | Pattern | Trigger | Labs |
|---|---|---|---|
| 1.1 | Read/write pointers | "in place," "return k," sorted input | 01–04 |
| 1.2 | Counting and voting | "more than n/2," "at least h with h" | 05–06 |
| 1.3 | Index math and reversal | "rotate," "circular," "wrap" | 07 |
| 1.4 | Best-so-far scan | "best pair, one before the other" | 08–09 |
| 1.5 | Reach and greedy choice | "can you reach," "fewest jumps," "circular route" | 10–12 |
| 1.6 | Prefix and suffix passes | "for each i, everything else" | 13–15 |
| 1.7 | List + dict design | "O(1) insert, delete, and random" | 16 |
| 1.8 | String processing | words, prefixes, symbols, layouts | 17–24 |

## Before you start

- Section 00 gate passed (or its diagnostic at 85%+).
- Import `anki/section-01.apkg`. New cards unlock lesson by lesson (tags `L1.1` ... `L1.8`); see the tip below.
- Do the [cumulative review](../../review/README.md) for section 01 first: review track `before-s01`, the quiz set to "01," and `python tools/review.py 1`.

> **Anki tip:** to study only what you've reached, use a filtered deck with search
> `deck:"DSA Mastery::01 Array-String" (tag:L1.1 OR tag:L1.2)` and add lesson tags as you go.
> Or just study the whole deck. Cards for later lessons are a useful preview.

## The path

Tiers: **Core** (easy) · **Build** (medium) · **Stretch** (hard) · **Bug Hunt**.
Give each problem a real fight before the hint ladder: about 15 / 25 / 40 minutes by tier.

### Week 1 — in place, counting, rotation, scans

| # | Do this | Kind of time |
|---|---|---|
| 1 | Listen: **01-1 Primer** | drive |
| 2 | Lesson 1.1 → labs **01, 02, 03** (Core) → lab **04** (Build) | desk |
| 3 | Listen: **01-2 In Place, Counting, Rotation, Scans** | drive |
| 4 | Lesson 1.2 → labs **05** (Core), **06** (Build) | desk |
| 5 | Lesson 1.3 → lab **07** (Build) | desk |
| 6 | Lesson 1.4 → labs **08** (Core), **09** (Build) | desk |
| 7 | Lab **25** Bug Hunt | desk |
| 8 | Lab **00** questions t1–t5 | break |

### Week 2 — reach, prefix/suffix, design

| # | Do this | Kind of time |
|---|---|---|
| 9 | Listen: **01-3 Reach, Prefix and Suffix, Design** | drive |
| 10 | Lesson 1.5 → labs **10, 11, 12** (Build) | desk |
| 11 | Lesson 1.6 → lab **13** (Build) → labs **14, 15** (Stretch) | desk |
| 12 | Lesson 1.7 → lab **16** (Build) | desk |
| 13 | Lab **00** questions t6–t8 | break |

### Week 3 — strings, then prove it

| # | Do this | Kind of time |
|---|---|---|
| 14 | Listen: **01-4 Strings** | drive |
| 15 | Lesson 1.8 → labs **17, 18, 20, 21** (Core) → **19, 22, 23** (Build) → **24** (Stretch) | desk |
| 16 | Lab **00** questions t9–t10 | break |
| 17 | Listen: **01-5 Rapid-Fire Drill** on repeat | drive |
| 18 | Q&A session with Claude (`qa-session.md`) | desk |
| 19 | Checkpoint quiz (`quiz/quiz.html`) | break |
| 20 | Repair: redo labs for weak topics, add cards for new mistakes | desk |
| 21 | Mastery gate | desk |

Run `python tools/run_labs.py sections/01-array-string` any time for a scoreboard.

## Mastery gate

Wait **two days** after your last lab. Blank file. No notes, hints, or AI. Timer on.

1. **Quiz:** 85% or better on `quiz/quiz.html`.
2. **Coverage:** every Core lab solved. At least 9 of 12 Build labs solved without Hint 3. At least one Stretch lab solved.
3. **Cold solves** — pick by rolling a die or with `python -c "import random; print(random.randint(1, 24))"`, rerolling for the right tier:
   - one Core problem in **15 minutes**
   - one Build problem in **25 minutes**
   - one more Build problem in **25 minutes**, while talking out loud the whole time
4. **Explain:** for each of the seven patterns, say the trigger and the core idea in under 30 seconds.

Pass all four: mark Section 01 complete in PROGRESS.md and start Section 02.
Miss one: redo that piece in two days. Don't move on with a hole. Section 02 builds on 1.1 and 1.6 directly.

## Extra reps (optional, before the gate)

- NeetCode: 49 Group Anagrams, 347 Top K Frequent Elements, 271 Encode and Decode Strings
- Codility Lessons: 2 (CyclicRotation, OddOccurrencesInArray), 4 (PermCheck, MissingInteger), 5 (PassingCars), 16 (MaxNonoverlappingSegments)

These use the same patterns with different wording. Great for interleaving.

## What's coming back later

| Problem | Returns in |
|---|---|
| Trapping Rain Water | Section 02 (two-pointer O(1) space) |
| Rotate Array | Section 04 (Rotate Image uses the reversal trick) |
| Insert Delete GetRandom | Section 08 (LRU Cache uses the same "two structures" idea) |
| Jump Game II | Section 13 (the ring idea becomes real BFS) |
| Best Time to Buy and Sell Stock | Sections 17 and 23 (Kadane and DP versions) |
