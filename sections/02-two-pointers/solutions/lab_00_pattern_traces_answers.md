# Lab 2.00 — Pattern Traces: Answers

| Q | Answer | Why |
|---|---|---|
| t1 | `[[0, 5], [1, 4], [2, 3]]` | Both move inward each step. After (2, 3) they'd be (3, 2), and `left < right` fails. |
| t2 | `True` | 'b' matches at index 1 of t, 'd' at index 3. Order is kept. |
| t3 | `[2, 3]` | 1 + 8 = 9 too big → right moves. 1 + 4 = 5 too small → left moves. 3 + 4 = 7. Positions 2 and 3 (1-indexed). |
| t4 | `3` | Three checks: (1, 8), (1, 4), (3, 4). |
| t5 | `[0, 4]` | Width 4 × min(4, 4) = 16. Nothing else comes close. |
| t6 | `2` | Lines 0 and 2: width 2 × min(1, 1) = 2. |
| t7 | `[[-2, 0, 2], [-2, 1, 1]]` | Fix −2, then two pointers find 0 + 2 and 1 + 1. |
| t8 | `2` | `[-1, -1, 2]` and `[-1, 0, 1]`. The second −1 is skipped as a repeat fixed value. |
