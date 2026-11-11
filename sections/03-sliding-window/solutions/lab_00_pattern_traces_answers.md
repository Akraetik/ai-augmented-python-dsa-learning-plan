# Lab 3.00 — Pattern Traces: Answers

| Q | Answer | Why |
|---|---|---|
| t1 | `[8, 7, 9, 6]` | 2+1+5, then +1−2, then +3−1, then +2−5. |
| t2 | `9` | The window `[5, 1, 3]`. |
| t3 | `3` | `"vdf"`. When the second `d` enters, shrink past the FIRST `d` only, not the whole window. |
| t4 | `4` | Indexes 2, 3, 4, 5. Length is `right - left + 1`. |
| t5 | `4` | `[1, 0, 1, 1]` (indexes 0–3) or `[1, 1, 0, 1]` (indexes 2–5). Each has one zero. |
| t6 | `1` | `[8]` alone is ≥ 7. |
| t7 | `"ACB"` | Indexes 5–7. Every other window with A, B and C is longer. |
| t8 | `[0, 3]` | `"catdog"` at 0 and `"dogcat"` at 3. At 6, `"catcat"` has no `dog`. |
