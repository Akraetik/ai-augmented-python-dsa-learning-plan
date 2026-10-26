"""
run_labs.py — run every lab in a section and print a scoreboard.

Usage:  python tools/run_labs.py sections/01-array-string
"""
import pathlib
import subprocess
import sys


def main(section):
    labs = sorted((pathlib.Path(section) / "labs").glob("lab_*.py"))
    solved = 0
    print(f"{'Lab':48s} Result")
    print("-" * 64)
    for lab in labs:
        try:
            p = subprocess.run([sys.executable, lab.name], cwd=lab.parent, capture_output=True,
                               text=True, timeout=120)
            out = p.stdout
            last = [l for l in out.splitlines() if "passed" in l or "correct" in l]
            ok = p.returncode == 0 and ("Solved." in out or ("correct" in out and "/" in out and _all(out)))
            summary = _strip(last[-1]) if last else "error: " + (p.stderr.strip().splitlines() or ["?"])[-1]
        except subprocess.TimeoutExpired:
            ok, summary = False, "timed out (infinite loop?)"
        solved += ok
        print(f"{lab.name:48s} {'SOLVED ' if ok else '       '}{summary}")
    print("-" * 64)
    print(f"{solved}/{len(labs)} solved")


def _all(out):
    import re
    m = re.findall(r"(\d+)/(\d+) correct", _strip(out))
    return bool(m) and m[-1][0] == m[-1][1]


def _strip(text):
    import re
    return re.sub(r"\x1b\[[0-9;]*m", "", text)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
