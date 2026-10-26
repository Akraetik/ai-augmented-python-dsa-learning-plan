# Lab 1.00 — Pattern Traces: Answers

| Q | Answer | Why |
|---|---|---|
| t1 | `3` | Three evens kept: 4, 6, 6. |
| t2 | `[4, 6, 6, 6, 3]` | Slots 0–2 were overwritten with 4, 6, 6. Slots 3–4 are untouched leftovers. |
| t3 | `4` | Candidate goes 3 → (count hits 0) → 4, and 4 survives to the end. |
| t4 | `2` | (5 + 4) % 7 = 9 % 7 = 2. |
| t5 | `2` | Best is 4 → 6 (or 1 → 3). Both give 2. |
| t6 | `[-inf, 2, 5, 5]` | Record first, then include: index 0 has nothing to its left. |
| t7 | `[1, 2, 6]` | Empty product is 1; then 2; then 2 × 3. |
| t8 | `False` | Reach is 1 after index 0; index 1 adds nothing; index 2 is beyond reach. |
| t9 | `"ACEBD"` | Row 0 gets A, C, E. Row 1 gets B, D. |
| t10 | `14` | X = 10, then I before V subtracts: 10 − 1 + 5. |
