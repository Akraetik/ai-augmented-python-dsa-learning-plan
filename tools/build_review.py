"""
build_review.py — build the cumulative review/ material from every finished section.

Writes:
  review/quiz.html                    one quiz page: pick the section you're STARTING, it samples
                                      questions from all earlier sections, tapered by age, and
                                      boosts questions you missed last time
  review/audio/scripts/before-sNN.txt rapid-fire review script for the week you start section NN
  (then run tools/build_audio.py review to render the MP3s)

The taper (how much of each past section you see):
  1 section back   ->  100%  of the base amount
  2 sections back  ->   60%
  3 sections back  ->   40%
  4+ sections back ->   25%  (never zero: old material keeps coming back, just less)

Usage:  python tools/build_review.py
"""
import importlib.util
import json
import pathlib
import random
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
TAPER = {1: 1.0, 2: 0.6, 3: 0.4}
FLOOR = 0.25
QUIZ_BASE = 10        # questions from the section just finished
AUDIO_BASE = 30       # Q&A pairs from the section just finished


def taper(age):
    return TAPER.get(age, FLOOR)


def sections():
    out = []
    for d in sorted((ROOT / "sections").iterdir()):
        m = re.match(r"(\d\d)-(.+)", d.name)
        if m and (d / "quiz" / "quiz_data.py").exists():
            out.append((int(m.group(1)), d))
    return out


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def quiz_page(secs):
    bank = []
    names = {}
    for num, d in secs:
        qd = load(d / "quiz" / "quiz_data.py", f"q{num}")
        label = d.name.split("-", 1)[1].replace("-", " ").title()
        names[num] = f"{num:02d} {label}"
        for q in qd.QUESTIONS:
            q = dict(q)
            q["section"] = num
            q["topic_label"] = qd.TOPICS[q["topic"]]
            q["study"] = f"Section {num:02d} · " + (q.get("study") or qd.REVIEW.get(q["topic"], ""))
            bank.append(q)
    data = {"bank": bank, "names": names, "taper": TAPER, "floor": FLOOR, "base": QUIZ_BASE,
            "max_section": max(names) + 1}
    tpl = (ROOT / "tools" / "review_quiz_template.html").read_text(encoding="utf-8")
    (ROOT / "review" / "quiz.html").write_text(tpl.replace("__DATA__", json.dumps(data)), encoding="utf-8")
    print(f"review/quiz.html: {len(bank)} questions from {len(secs)} sections")


def drill_pairs(d):
    """Pull (question, answer) pairs out of a section's rapid-fire audio script."""
    scripts = sorted((d / "audio" / "scripts").glob("*rapid-fire*.txt"))
    pairs = []
    for s in scripts:
        lines = [l.strip() for l in s.read_text(encoding="utf-8").splitlines() if l.strip()]
        for i, line in enumerate(lines):
            if line.startswith("N:") and i + 2 < len(lines) and lines[i + 1].startswith("[pause") \
                    and lines[i + 2].startswith("A:"):
                pairs.append((line[2:].strip(), lines[i + 1], lines[i + 2][2:].strip()))
    return pairs


def audio_scripts(secs):
    out_dir = ROOT / "review" / "audio" / "scripts"
    out_dir.mkdir(parents=True, exist_ok=True)
    by_num = dict(secs)
    for start in range(1, max(by_num) + 2):
        past = [n for n in by_num if n < start]
        if not past:
            continue
        rng = random.Random(start)
        lines = [f"# Review before Section {start:02d}",
                 f"N: Cumulative review. You're about to start section {start}. "
                 "This track mixes questions from every section you've finished. "
                 "The newest gets the most time. Older ones come back less often, but they always come back.",
                 "N: Say each answer out loud before you hear it.", "[pause 2]"]
        total = 0
        for n in sorted(past, reverse=True):
            age = start - n
            pairs = drill_pairs(by_num[n])
            k = min(len(pairs), max(4, round(AUDIO_BASE * taper(age))))
            picked = rng.sample(pairs, k)
            name = by_num[n].name.split("-", 1)[1].replace("-", " ")
            lines.append(f"N: From section {n}, {name}. {k} questions.")
            lines.append("[pause 1]")
            for q, pause, a in picked:
                lines += [f"N: {q}", pause, f"A: {a}"]
            lines.append("[pause 1]")
            total += k
        lines.append(f"N: End of review. {total} questions. Missed any? Find them in the review sheets, then start section {start}.")
        (out_dir / f"before-s{start:02d}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"review/audio/scripts/before-s{start:02d}.txt: {total} questions")


def main():
    secs = sections()
    (ROOT / "review").mkdir(exist_ok=True)
    quiz_page(secs)
    audio_scripts(secs)


if __name__ == "__main__":
    main()
