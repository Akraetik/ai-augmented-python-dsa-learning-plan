"""
SOLUTION — Lab 1.23 Zigzag Conversion (LeetCode 6)
Time O(n). Space O(n).
One list per row. Walk the string; put each char in the current row; flip direction at the top and
bottom rows. num_rows == 1 (or >= len(s)) returns s unchanged — otherwise the step logic breaks.
"""


def convert(s: str, num_rows: int) -> str:
    if num_rows == 1 or num_rows >= len(s):
        return s
    rows = [[] for _ in range(num_rows)]
    row, step = 0, 1
    for ch in s:
        rows[row].append(ch)
        if row == 0:
            step = 1
        elif row == num_rows - 1:
            step = -1
        row += step
    return "".join("".join(r) for r in rows)
