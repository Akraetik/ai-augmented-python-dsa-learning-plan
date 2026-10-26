"""
LAB 1.16 — Insert Delete GetRandom O(1)                      Tier: Build
LeetCode 380 (Medium) — https://leetcode.com/problems/insert-delete-getrandom-o1/
Lesson 1.7 · Pattern: list + dict(value -> index); delete by swapping with the last item

THE PROBLEM (in our words)
Build a class RandomizedSet:
  insert(val)   -> bool   add val if it's missing; True if added, False if it was already there
  remove(val)   -> bool   remove val if present; True if removed, False if it wasn't there
  getRandom()   -> int    return a random current element, each one equally likely
Every method must be O(1) on average.

RETURNS: see each method. getRandom is only called when the set is not empty.

EXAMPLE
  s = RandomizedSet()
  s.insert(1)   -> True
  s.remove(2)   -> False
  s.insert(2)   -> True
  s.getRandom() -> 1 or 2
  s.remove(1)   -> True
  s.insert(2)   -> False
  s.getRandom() -> 2

BEFORE YOU CODE
  Write Lesson 1.7's five remove steps in your PLAN. Trace removing the LAST item. Does your order still work?
  Use `import random` and random.choice(...) on the list.
"""
import random

# PLAN
# What __init__ stores:
# insert steps:
# remove steps (5):
# getRandom:


class RandomizedSet:
    def __init__(self):
        pass

    def insert(self, val: int) -> bool:
        pass

    def remove(self, val: int) -> bool:
        pass

    def getRandom(self) -> int:
        pass


# ---------- tests: don't edit below ----------
from _check import check

ENTRY = "RandomizedSet"


def _simulate(cls, ops, args):
    """Run a list of operations. getRandom results are checked for membership, then recorded as 'ok'."""
    obj = cls()
    out = [None]
    shadow = set()
    for op, a in zip(ops[1:], args[1:]):
        if op == "insert":
            out.append(obj.insert(*a))
            shadow.add(a[0])
        elif op == "remove":
            out.append(obj.remove(*a))
            shadow.discard(a[0])
        elif op == "getRandom":
            got = obj.getRandom()
            out.append("ok" if got in shadow else f"bad:{got}")
    return out


def _runner(cls):
    def run(ops, args):
        return _simulate(cls, ops, args)
    run.__name__ = cls.__name__ if hasattr(cls, "__name__") else "RandomizedSet"
    return run


CASES = [
    ((["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"],
      [[], [1], [2], [2], [], [1], [2], []]),
     [None, True, False, True, "ok", True, False, "ok"], "example"),
    ((["RandomizedSet", "insert", "insert", "remove", "remove", "insert", "getRandom"],
      [[], [5], [5], [5], [5], [7], []]),
     [None, True, False, True, False, True, "ok"], "double insert / double remove"),
    ((["RandomizedSet", "insert", "insert", "insert", "remove", "remove", "getRandom", "getRandom"],
      [[], [10], [20], [30], [10], [30], [], []]),
     [None, True, True, True, True, True, "ok", "ok"], "remove first and last"),
    ((["RandomizedSet", "insert", "remove", "insert", "getRandom"],
      [[], [-1], [-1], [-1], []]),
     [None, True, True, True, "ok"], "remove then re-add"),
]


def _perf_args():
    ops, args = ["RandomizedSet"], [[]]
    for i in range(60_000):
        ops.append("insert"); args.append([i])
    for i in range(0, 60_000, 2):
        ops.append("remove"); args.append([i])
    for _ in range(20_000):
        ops.append("getRandom"); args.append([])
    return (ops, args)


PERF = [("110,000 operations", _perf_args, 1.5)]


def _fair(cls):
    """getRandom should hit every element over many calls."""
    obj = cls()
    for v in (1, 2, 3):
        obj.insert(v)
    seen = {obj.getRandom() for _ in range(300)}
    return seen == {1, 2, 3}


def run_tests(cls):
    ok = check(_runner(cls), CASES, perf=PERF, title="RandomizedSet")
    try:
        fair = _fair(cls)
    except Exception:
        fair = False
    print(("PASS" if fair else "FAIL") + " getRandom is random (hits all of {1, 2, 3} in 300 calls)")
    return ok and fair


if __name__ == "__main__":
    run_tests(RandomizedSet)
