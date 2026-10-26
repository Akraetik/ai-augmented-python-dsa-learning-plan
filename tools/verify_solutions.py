"""
verify_solutions.py — maintainer tool.
For every lab in a section, checks that:
  1. the official solution passes every test (including speed), and
  2. the starter code does NOT pass (so the lab actually tests something).

Usage:  python tools/verify_solutions.py sections/01-array-string
"""
import pathlib
import subprocess
import sys

RUNNER = r'''
import importlib.util, sys, io, contextlib
lab_path, sol_path, mode = sys.argv[1], sys.argv[2], sys.argv[3]
sys.path.insert(0, str(__import__("pathlib").Path(lab_path).parent))
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    lab = load("lab", lab_path)
    if mode == "solution":
        sol = load("sol", sol_path)
        target = getattr(sol, lab.ENTRY)
    else:
        target = getattr(lab, lab.ENTRY)
    ok = lab.run_tests(target)
print("RESULT", bool(ok))
if not ok and mode == "solution":
    print(buf.getvalue())
'''


def main(section):
    section = pathlib.Path(section)
    labs = sorted((section / "labs").glob("lab_*.py"))
    bad = 0
    for lab in labs:
        sol = section / "solutions" / (lab.stem + "_solution.py")
        if not sol.exists():
            print(f"MISSING SOLUTION  {lab.name}")
            bad += 1
            continue
        res = {}
        for mode in ("solution", "starter"):
            p = subprocess.run([sys.executable, "-c", RUNNER, str(lab), str(sol), mode],
                               capture_output=True, text=True, timeout=300)
            out = p.stdout + p.stderr
            res[mode] = ("RESULT True" in out, out)
        sol_ok, sol_out = res["solution"]
        starter_ok, _ = res["starter"]
        status = "OK " if sol_ok and not starter_ok else "BAD"
        if status == "BAD":
            bad += 1
        print(f"{status} {lab.name:45s} solution={'pass' if sol_ok else 'FAIL'}  starter={'pass(!)' if starter_ok else 'fails'}")
        if not sol_ok:
            print(sol_out[-3000:])
    print(f"\n{len(labs) - bad}/{len(labs)} labs verified")
    return bad == 0


if __name__ == "__main__":
    sys.exit(0 if main(sys.argv[1]) else 1)
