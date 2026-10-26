"""
SOLUTION — Lab 1.24 Text Justification (LeetCode 68)
Time O(total characters). Space O(max_width) per line.

1. Greedy pack: add words while letters + (words - 1) spaces <= max_width.
2. Full line: spread (max_width - letters) spaces over (words - 1) gaps.
   divmod gives the base gap size and how many LEFT gaps get one extra.
3. Last line or single word: join with single spaces, pad on the right.
"""
from typing import List


def _left(line: List[str], width: int) -> str:
    text = " ".join(line)
    return text + " " * (width - len(text))


def _justify(line: List[str], width: int) -> str:
    if len(line) == 1:
        return _left(line, width)
    gaps = len(line) - 1
    spaces = width - sum(len(w) for w in line)
    base, extra = divmod(spaces, gaps)
    parts = []
    for i, word in enumerate(line[:-1]):
        parts.append(word)
        parts.append(" " * (base + (1 if i < extra else 0)))
    parts.append(line[-1])
    return "".join(parts)


def full_justify(words: List[str], max_width: int) -> List[str]:
    out = []
    i, n = 0, len(words)
    while i < n:
        line = [words[i]]
        letters = len(words[i])
        j = i + 1
        while j < n and letters + len(words[j]) + len(line) <= max_width:
            line.append(words[j])
            letters += len(words[j])
            j += 1
        out.append(_left(line, max_width) if j == n else _justify(line, max_width))
        i = j
    return out
