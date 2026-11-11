"""
SOLUTION — Lab 3.09 Bug Hunt: Longest Substring Without Repeating

The four bugs:
1. `if s[right] in seen:` shrinks only ONE step.      -> NEW: `if` instead of `while` when shrinking.
   The duplicate may be further in. Keep shrinking until it's gone. Check: "Is the window valid
   NOW, or did I only take one step toward valid?"  Candidate M9.
2. `left + 1` is never saved.                         -> M4. Fix: left += 1
3. `right - left` undercounts by one.                 -> M5. Fix: right - left + 1
4. `return best` is inside the loop.                  -> M7. Fix: dedent it below the loop.
"""


def longest(s: str) -> int:
    seen = set()
    left = 0
    best = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        best = max(best, right - left + 1)
    return best
