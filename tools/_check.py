"""
_check.py — the tiny test runner every lab uses.

You never need to edit this file. A copy lives in each section's labs/ folder
so that `python lab_xx.py` works from any IDE with no setup.

What it does:
  * runs your function on each test case
  * shows input, expected, and what you returned when a test fails
  * copies inputs first, so one test can't break the next
  * checks in-place problems by looking at the list you changed
  * runs big "performance" inputs with a time limit, like Codility's hidden tests
"""
import copy
import os
import pathlib
import sys
import threading
import time

# Turn on ANSI colors in the Windows console. Harmless elsewhere.
if os.name == "nt":
    os.system("")

_USE_COLOR = sys.stdout.isatty() or "PYCHARM_HOSTED" in os.environ or "VSCODE_PID" in os.environ
G = "\033[92m" if _USE_COLOR else ""
R = "\033[91m" if _USE_COLOR else ""
Y = "\033[93m" if _USE_COLOR else ""
D = "\033[2m" if _USE_COLOR else ""
B = "\033[1m" if _USE_COLOR else ""
X = "\033[0m" if _USE_COLOR else ""

_MAX_SHOW = 200
CASE_TIMEOUT = 5  # seconds per small test before calling it an infinite loop
_STUDY_G = None  # characters of a value to print before trimming


def _show(value):
    text = repr(value)
    if len(text) > _MAX_SHOW:
        text = text[:_MAX_SHOW] + f"... ({len(text)} chars)"
    return text


def _normalize(case):
    """Accept (args, expected) or (args, expected, label) or a dict."""
    if isinstance(case, dict):
        args = case["args"]
        expected = case["expected"]
        label = case.get("label", "")
    elif len(case) == 3:
        args, expected, label = case
    else:
        args, expected = case
        label = ""
    if not isinstance(args, tuple):
        args = (args,)
    return args, expected, label


def _caller_globals():
    import inspect
    for frame_info in inspect.stack()[2:]:
        g = frame_info.frame.f_globals
        if g.get("__name__") != __name__:
            return g
    return {}


def _lesson_pointer(g):
    """Find 'Lesson 1.1 · Pattern: ...' in the lab's docstring and turn it into file paths."""
    import re
    doc = g.get("__doc__") or ""
    lab_file = g.get("__file__")
    m = re.search(r"Lessons?:?\s*([0-9][0-9.]*(?:\s*(?:,|and|–|-)\s*[0-9][0-9.]*)*)(.*)", doc)
    if not m:
        return None
    nums = re.findall(r"[0-9]+\.[0-9]+", m.group(1))
    pattern = re.sub(r"^Pattern:\s*", "", m.group(2).strip(" ·:")).strip("()")
    if re.fullmatch(r"and MISTAKES\.md", pattern):
        pattern = ""
    files = []
    if lab_file:
        here = pathlib.Path(lab_file).resolve()
        lesson_dir, prefix = here.parent.parent / "lessons", "lessons/"
        sec = re.match(r"s(\d\d)_", here.name)
        if sec:  # a cold-solve copy in review/cold-solves/: point back to the section
            for root in here.parents:
                found = sorted((root / "sections").glob(f"{sec.group(1)}-*")) if (root / "sections").is_dir() else []
                if found:
                    lesson_dir, prefix = found[0] / "lessons", f"sections/{found[0].name}/lessons/"
                    break
        for n in nums:
            hit = sorted(lesson_dir.glob(f"{n}-*.md"))
            files.append(f"{prefix}{hit[0].name}" if hit else f"lesson {n}")
    return files, pattern


def _print_study(g, extra=None):
    import re
    found = _lesson_pointer(g)
    lab = re.sub(r"^s\d\d_", "", pathlib.Path(g.get("__file__", "this lab")).stem)
    print(f"{Y}{B}STUDY{X}{Y} before you retry:{X}")
    if found:
        files, pattern = found
        for f in files:
            print(f"  {Y}- re-read {f}{X}")
        if pattern:
            print(f"  {Y}- focus on: {pattern}{X}")
        if extra and pattern and "Hidden loops" in pattern:
            extra = None
    if extra:
        print(f"  {Y}- {extra}{X}")
    print(f"  {Y}- hints.md → {lab}: open ONE hint{X}")
    print(f"  {Y}- check your code against MISTAKES.md (M1–M7){X}")


def check(fn, cases, *, inplace=None, compare=None, perf=None, title=None):
    """
    Run `fn` against `cases`. Returns True only if every test passes.

    cases    list of (args_tuple, expected[, label])
    inplace  int  -> compare args[inplace] after the call, not the return value
             callable(args, returned) -> value to compare
    compare  callable(got, expected) -> bool, for answers with more than one right form
    perf     list of (label, make_args, seconds). make_args() builds a big input.
    """
    title = title or getattr(fn, "__name__", "solution")
    print(f"\n{B}Testing {title}{X}")
    print(D + "-" * 60 + X)

    passed = 0
    total = len(cases)
    returned_none = 0

    for i, case in enumerate(cases, 1):
        args, expected, label = _normalize(case)
        call_args = copy.deepcopy(args)
        tag = f"Test {i}" + (f" ({label})" if label else "")
        box = {}

        def _run():
            try:
                box["ret"] = fn(*call_args)
            except Exception as e:  # show the error, keep going
                box["err"] = e

        worker = threading.Thread(target=_run, daemon=True)
        worker.start()
        worker.join(CASE_TIMEOUT)
        if worker.is_alive():
            print(f"{R}FAIL{X} {tag}")
            print(f"     input:    {_show(args)}")
            print(f"     {R}still running after {CASE_TIMEOUT}s on a SMALL input: almost certainly an infinite loop.{X}")
            print(f"     {Y}Look for a while loop whose pointer never changes (M4: `left + 1` instead of `left += 1`),{X}")
            print(f"     {Y}or pointers that move the wrong way so the loop never ends.{X}")
            print(D + "-" * 60 + X)
            _print_study(_caller_globals())
            sys.stdout.flush()
            os._exit(1)
        if "err" in box:
            e = box["err"]
            print(f"{R}FAIL{X} {tag}")
            print(f"     input:    {_show(args)}")
            print(f"     {R}crashed:  {type(e).__name__}: {e}{X}")
            continue
        returned = box.get("ret")

        if inplace is None:
            got = returned
        elif callable(inplace):
            got = inplace(call_args, returned)
        else:
            got = call_args[inplace]

        if returned is None and inplace is None and expected is not None:
            returned_none += 1

        ok = compare(got, expected) if compare else got == expected
        if ok:
            passed += 1
            print(f"{G}PASS{X} {tag}")
        else:
            print(f"{R}FAIL{X} {tag}")
            print(f"     input:    {_show(args)}")
            print(f"     expected: {_show(expected)}")
            print(f"     got:      {_show(got)}")

    if returned_none == total and total:
        print(f"\n{Y}Every test returned None.{X} Did you write `return`? (Mistake M6: read the return type.)")

    perf_ok = True
    global _STUDY_G
    _STUDY_G = _caller_globals()
    if perf and passed == total:
        perf_ok = _run_perf(fn, perf)
    elif perf:
        print(f"{D}Performance tests skip until all correctness tests pass.{X}")

    print(D + "-" * 60 + X)
    all_ok = passed == total and perf_ok
    color = G if all_ok else R
    perf_note = "" if not perf else ("  |  speed: OK" if perf_ok and passed == total else "  |  speed: not checked" if passed != total else "  |  speed: TOO SLOW")
    print(f"{color}{B}{passed}/{total} correctness tests passed{perf_note}{X}")
    if all_ok:
        print(f"{G}Solved. Now: compare with the solution, log any new mistake, and add a card if you learned something.{X}")
    else:
        slow_only = passed == total and not perf_ok
        _print_study(_caller_globals(),
                     extra="lesson 00.2 'Hidden loops in Python' table — what work are you repeating?" if slow_only else None)
    return all_ok


def _run_perf(fn, perf):
    ok = True
    for label, make_args, limit in perf:
        args = make_args()
        if not isinstance(args, tuple):
            args = (args,)
        result = {}

        def target():
            start = time.perf_counter()
            try:
                fn(*args)
            except Exception as e:
                result["error"] = e
            result["time"] = time.perf_counter() - start

        t = threading.Thread(target=target, daemon=True)
        t.start()
        t.join(limit * 4)  # wait a bit past the limit before giving up
        if t.is_alive():
            print(f"{R}SLOW{X} {label}: still running after {limit * 4:.0f}s (limit {limit}s).")
            print(f"     {Y}Likely O(n^2) or worse. Look for a loop inside a loop, `in` on a list, pop(0), or slicing inside a loop.{X}")
            _finish_and_exit(_STUDY_G)
        if "error" in result:
            print(f"{R}FAIL{X} {label}: crashed on big input: {type(result['error']).__name__}: {result['error']}")
            ok = False
        elif result["time"] > limit:
            print(f"{R}SLOW{X} {label}: {result['time']:.2f}s (limit {limit}s)")
            print(f"     {Y}Correct but too slow. Codility would fail this. What work are you repeating?{X}")
            ok = False
        else:
            print(f"{G}FAST{X} {label}: {result['time']:.3f}s (limit {limit}s)")
    return ok


def _finish_and_exit(g=None):
    print(D + "-" * 60 + X)
    print(f"{R}{B}Correct on small tests, but too slow on big ones.{X}")
    if g:
        _print_study(g, extra="lesson 00.2 'Hidden loops in Python' table — what work are you repeating?")
    sys.stdout.flush()
    os._exit(1)


def _norm_answer(value):
    """Lower-case, drop spaces, so 'O(n log n)' == 'o(nlogn)'."""
    text = "".join(str(value).lower().split())
    return text.replace("^", "**").replace("²", "**2").replace("³", "**3").replace("'", '"')


def answer_hash(value, question=""):
    """Hash of a normalized answer, salted with the question id, so you can't peek."""
    import hashlib
    return hashlib.sha256((question + "|" + _norm_answer(value)).encode()).hexdigest()[:16]


def check_answers(answers, hashed_key, *, title="your answers", study=None):
    """
    For trace and Big-O labs. `hashed_key` maps question -> answer_hash(right answer).
    `study` maps question -> where to restudy it. Plain answers are in the section's solutions/ folder.
    """
    study = study or {}
    missed = []
    print(f"\n{B}Checking {title}{X}")
    print(D + "-" * 60 + X)
    passed = 0
    key = hashed_key
    for q, expected_hash in key.items():
        got = answers.get(q, ...)
        if got is ... or got == "":
            print(f"{Y}TODO{X} {q}: no answer yet")
        elif answer_hash(got, q) == expected_hash:
            passed += 1
            print(f"{G}PASS{X} {q}")
        else:
            print(f"{R}FAIL{X} {q}: you said {_show(got)}")
            if q in study:
                print(f"     {Y}study: {study[q]}{X}")
            missed.append(q)
    print(D + "-" * 60 + X)
    color = G if passed == len(key) else R
    print(f"{color}{B}{passed}/{len(key)} correct{X}")
    if missed:
        print(f"{Y}{B}STUDY{X}{Y} for the ones you missed:{X}")
        print(f"  {Y}1. Copy that question's code into a scratch file. Run it. Add print() lines until you see why.{X}")
        topics = []
        for q in missed:
            if q in study and study[q] not in topics:
                topics.append(study[q])
        for t in topics:
            print(f"  {Y}- {t}{X}")
        print(f"  {Y}2. Fix your answer and run this file again.{X}")
        print(f"  {Y}3. Missed it twice? Add it to MISTAKES.md and make a flashcard.{X}")
    return passed == len(key)
