# Putting This Course on GitHub

Windows PowerShell steps. Same Git workflow as the Network+ study kit.

## First time: create the repo

1. **Unzip** `ai-augmented-python-dsa-learning-plan.zip` into `C:\Users\learn\Documents\`.
   You should end up with `C:\Users\learn\Documents\ai-augmented-python-dsa-learning-plan\README.md`.
   (If you unzipped an earlier zip, delete that older folder first. This zip has everything.)

2. **The repo on GitHub** is `Akraetik/ai-augmented-python-dsa-learning-plan` (already created).
   If it isn't empty (GitHub added a README or license), see "If the push is rejected" below.

3. **Push it:**

   ```powershell
   cd C:\Users\learn\Documents\ai-augmented-python-dsa-learning-plan
   git init
   git add .
   git commit -m "Sections 00-02, review system, iteration log"
   git branch -M main
   git remote add origin https://github.com/Akraetik/ai-augmented-python-dsa-learning-plan.git
   git push -u origin main
   ```

4. **Check it:** refresh the repo page. The README shows the study-flow chart. `ITERATIONS.md` is the change log
   and feedback log. `review/` is the cumulative review.

### If the push is rejected

That means GitHub already has a commit (a README or license added when the repo was created). Merge it in, then push:

```powershell
git pull origin main --allow-unrelated-histories
# if a README conflict appears: keep ours
git checkout --ours README.md ; git add README.md ; git commit -m "Merge GitHub starter files"
git push -u origin main
```

## Every week after that

### Your own progress (PROGRESS.md, MISTAKES.md, REVIEW-LOG.md, lab files)

```powershell
cd C:\Users\learn\Documents\ai-augmented-python-dsa-learning-plan
git add .
git commit -m "Week of 2026-11-02: Section 02 labs, review before s03"
git push
```

**Lab files:** you'll type solutions into the lab files. That's fine to commit. It shows your work.
If you'd rather keep the starter files clean, work in a branch:

```powershell
git switch -c my-work      # once
git add . ; git commit -m "Solved labs 01-05" ; git push -u origin my-work
```

### A new section from Claude

Claude will send a zip with only the new and changed files. Unzip it **over** the repo folder, then:

```powershell
git switch -c section-03
git add .
git commit -m "Add Section 03 Sliding Window"
git push -u origin section-03
```

Open a pull request on GitHub, look over the changes, merge it, then:

```powershell
git switch main
git pull
```

Using a PR for each new section keeps a clean history: one PR per section, one per iteration.

## What's in the repo

| Path | What it is |
|---|---|
| `README.md` | Start here. Study-flow chart, how to run labs, section table. |
| `PROMPT.md` | The prompt that built the course, plus how to continue it. |
| `ITERATIONS.md` | **Change log + feedback log.** Every change, and what you said was good or needed work. |
| `METHOD.md` | Why the course is built this way. |
| `ROADMAP.md` | All 150 problems mapped to the 23 sections. |
| `PROGRESS.md` | Your tracker: labs, cold-solve dates, gates. |
| `MISTAKES.md` | Your repeat mistakes (M1–M7, candidate M8). |
| `review/` | Cumulative review. Grows every section; older sections taper. |
| `sections/NN-name/` | Lessons, labs, hints, solutions, Anki, audio, quiz, Q&A. |
| `tools/` | Test runner, deck/quiz/audio/review builders, cold-solve picker. |
| `docs/` | Study-flow chart and this guide. |

## Size

About 67 MB, mostly MP3s. GitHub's limit is 100 MB **per file**; the largest file here is under 7 MB.

## Making it public later

Settings → General → Danger Zone → Change visibility → Public. Before you do:
- Read `PROGRESS.md`, `MISTAKES.md`, and `review/REVIEW-LOG.md`. They're your personal logs. Keep or clear them.
- `PROMPT.md` and `ITERATIONS.md` are written to be shared. They show how the course was built.
