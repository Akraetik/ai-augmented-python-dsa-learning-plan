"""
review.py — pick this week's cold solves from earlier sections, tapered by age.

Usage:   python tools/review.py 2          (you're about to start section 02)

It copies blank starter files into review/cold-solves/<date>-before-sNN/ with the test runner,
and logs the picks in review/REVIEW-LOG.md. Solve them from a blank mind: no notes, no hints, timer on.

How many per past section:
  1 section back   -> 2 problems
  2 sections back  -> 1 problem
  3+ sections back -> 1 problem from every other older section, rotating week to week
Warm-up labs are skipped. Problems you marked "assisted" in PROGRESS.md are picked first.
"""
import datetime
import pathlib
import random
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def labs(section_dir):
    out = []
    for p in sorted((section_dir / "labs").glob("lab_*.py")):
        head = p.read_text(encoding="utf-8").split("\n")[1]
        m = re.search(r"LAB [\d.]+ — (.+?)\s{2,}Tier: (.+)", head)
        if m and m.group(2).strip() != "Warm-up":
            out.append((p, m.group(1).strip(), m.group(2).strip()))
    return out


def assisted_titles():
    prog = ROOT / "PROGRESS.md"
    if not prog.exists():
        return set()
    hits = set()
    for line in prog.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.split("|")]
        if len(cells) > 3 and cells[3].lower() == "assisted":
            hits.add(cells[1][3:].strip())
    return hits


def main(start):
    secs = {}
    for d in sorted((ROOT / "sections").iterdir()):
        m = re.match(r"(\d\d)-", d.name)
        if m and int(m.group(1)) < start:
            secs[int(m.group(1))] = d
    if not secs:
        print("Nothing to review yet.")
        return
    rng = random.Random()
    assisted = assisted_titles()
    today = datetime.date.today().isoformat()
    dest = ROOT / "review" / "cold-solves" / f"{today}-before-s{start:02d}"
    dest.mkdir(parents=True, exist_ok=True)
    shutil.copy(ROOT / "tools" / "_check.py", dest / "_check.py")
    picks = []
    for n in sorted(secs, reverse=True):
        age = start - n
        if age == 1:
            k = 2
        elif age == 2:
            k = 1
        else:
            k = 1 if (n + start) % 2 == 0 else 0     # every other week, rotating
        pool = labs(secs[n])
        first = [x for x in pool if x[1] in assisted]
        rest = [x for x in pool if x[1] not in assisted]
        rng.shuffle(first)
        rng.shuffle(rest)
        picks += [(n, *x) for x in (first + rest)[:k]]
    print(f"Cold solves before section {start:02d} → {dest.relative_to(ROOT)}\n")
    for n, path, title, tier in picks:
        shutil.copy(path, dest / f"s{n:02d}_{path.name}")
        limit = {"Core": 15, "Build": 25, "Stretch": 40, "Bug Hunt": 20}.get(tier, 25)
        print(f"  S{n:02d}  {title}  ({tier}, {limit} min)")
    log = ROOT / "review" / "REVIEW-LOG.md"
    if not log.exists():
        log.write_text("# Review Log\n\n| Date | Before section | Cold solves | Quiz score | Notes |\n|---|---|---|---|---|\n",
                       encoding="utf-8")
    names = "; ".join(f"S{n:02d} {t}" for n, _, t, _ in picks)
    with open(log, "a", encoding="utf-8") as f:
        f.write(f"| {today} | {start:02d} | {names} | | |\n")
    print("\nNo notes, no hints, timer on. Fill in your quiz score in review/REVIEW-LOG.md.")


if __name__ == "__main__":
    main(int(sys.argv[1]))
