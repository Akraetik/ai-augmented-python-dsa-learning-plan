"""
build_audio.py — render a section's audio scripts to MP3 with Kokoro TTS (runs offline).

Script format (audio/scripts/*.txt):
    # Title line (not spoken; used for the MP3 title)
    N: narrator line
    A: answer-voice line (used for drills and examples)
    [pause 3]           silence, in seconds
    blank lines and lines starting with // are ignored

Setup (once):
    pip install kokoro-onnx soundfile
    download kokoro-v1.0.onnx and voices-v1.0.bin from
    https://github.com/thewh1teagle/kokoro-onnx/releases  (model-files-v1.0)
    put them in tools/models/  (or set KOKORO_DIR)
    ffmpeg must be on your PATH

Usage:  python tools/build_audio.py sections/01-array-string [script-name-filter]
"""
import os
import pathlib
import re
import subprocess
import sys
import tempfile

import numpy as np
import soundfile as sf

NARRATOR = "am_michael"
ANSWER = "af_heart"
SPEED = {"N": 0.92, "A": 0.95}
SR = 24000
GAP = 0.45  # seconds between lines

# Say tricky things the way a person would. Applied to every spoken line.
SAY = [
    (r"O\(n log n\)", "O of n log n"),
    (r"O\(n\^2\)|O\(n²\)", "O of n squared"),
    (r"O\(log n\)", "O of log n"),
    (r"O\(1\)", "O of one"),
    (r"O\(n\)", "O of n"),
    (r"O\(k\)", "O of k"),
    (r"\bi\+1\b", "i plus one"),
    (r"==", " equals "),
    (r"\bLeetCode\b", "Leet Code"),
    (r"\bNeetCode\b", "Neet Code"),
    (r"\bdict\b", "dictionary"),
    (r"\bdicts\b", "dictionaries"),
    (r"\bdeque\b", "deck"),
    (r"\bAnki\b", "Ahnkee"),
    (r"\bIDE\b", "I D E"),
    (r"\bstr\b", "string"),
]


def speakable(text):
    for pat, rep in SAY:
        text = re.sub(pat, rep, text)
    return text


def parse(path):
    title, items = path.stem, []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("//"):
            continue
        if line.startswith("# "):
            title = line[2:].strip()
            continue
        m = re.match(r"\[pause ([\d.]+)\]", line)
        if m:
            items.append(("P", float(m.group(1))))
            continue
        m = re.match(r"([NA]):\s*(.+)", line)
        if m:
            items.append((m.group(1), m.group(2)))
        else:
            raise ValueError(f"{path.name}: can't parse line: {raw}")
    return title, items


def render(kokoro, path, out_dir):
    title, items = parse(path)
    chunks = []
    for kind, val in items:
        if kind == "P":
            chunks.append(np.zeros(int(SR * val), dtype=np.float32))
            continue
        voice = NARRATOR if kind == "N" else ANSWER
        samples, sr = kokoro.create(speakable(val), voice=voice, speed=SPEED[kind], lang="en-us")
        assert sr == SR
        chunks.append(samples.astype(np.float32))
        chunks.append(np.zeros(int(SR * GAP), dtype=np.float32))
    audio = np.concatenate(chunks)
    peak = float(np.max(np.abs(audio))) or 1.0
    audio = audio / peak * 0.9
    with tempfile.TemporaryDirectory() as td:
        wav = pathlib.Path(td) / "out.wav"
        sf.write(wav, audio, SR)
        mp3 = out_dir / (path.stem + ".mp3")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav), "-ac", "1", "-b:a", "80k",
                        "-metadata", f"title={title}", "-metadata", "artist=AI-Augmented Python DSA Learning Plan",
                        "-metadata", "album=AI-Augmented Python DSA Learning Plan", str(mp3)], check=True)
    minutes = len(audio) / SR / 60
    print(f"  {mp3.name}: {minutes:.1f} min")
    return title, minutes


def write_transcript(path, out_dir):
    title, items = parse(path)
    lines = [f"# {title}\n"]
    for kind, val in items:
        if kind == "P":
            lines.append(f"*[pause {val:g}s]*\n")
        else:
            who = "**Narrator:**" if kind == "N" else "**Answer:**"
            lines.append(f"{who} {val}\n")
    (out_dir / "transcripts").mkdir(exist_ok=True)
    (out_dir / "transcripts" / (path.stem + ".md")).write_text("\n".join(lines), encoding="utf-8")


def main(section, only=None):
    from kokoro_onnx import Kokoro
    section = pathlib.Path(section)
    model_dir = pathlib.Path(os.environ.get("KOKORO_DIR", pathlib.Path(__file__).parent / "models"))
    kokoro = Kokoro(str(model_dir / "kokoro-v1.0.onnx"), str(model_dir / "voices-v1.0.bin"))
    out_dir = section / "audio"
    scripts = sorted((out_dir / "scripts").glob("*.txt"))
    for s in scripts:
        if only and only not in s.stem:
            continue
        print(f"rendering {s.name}")
        write_transcript(s, out_dir)
        render(kokoro, s, out_dir)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
