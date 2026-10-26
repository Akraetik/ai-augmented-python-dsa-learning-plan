"""
SOLUTION — Lab 1.22 Integer to Roman (LeetCode 12)
Time O(1) — at most ~15 symbols for 1..3999. Space O(1).
Greedy: take the biggest value that fits, repeat. The six subtract pairs are in the table,
so greedy never needs to "look ahead."
"""

PAIRS = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
         (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]


def int_to_roman(num: int) -> str:
    parts = []
    for value, symbol in PAIRS:
        count, num = divmod(num, value)
        parts.append(symbol * count)
    return "".join(parts)
