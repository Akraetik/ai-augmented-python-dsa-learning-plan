# Lab 0.00 — Trace It: Answers

| Q | Answer | Why |
|---|---|---|
| q1 | `[5, 9, 4]` | Adds each item's index to it: 5+0, 8+1, 2+2. |
| q2 | `"dcb"` | `s[1:4]` is `"bcd"` (stop index 4 not included), then reversed. |
| q3 | `15` | `range(2, 10, 3)` is 2, 5, 8. |
| q4 | `[2, 3]` | Indexes 1 and 2. Index 3 is the stop, so it's left out. |
| q5 | `4` | `y = x` doesn't copy. Both names point at the same list. |
| q6 | `3` | Integer division drops the remainder. |
| q7 | `-4` | `//` rounds **down**, toward negative infinity. -3.5 becomes -4. |
| q8 | `["Hello", "World"]` | `split()` with no argument splits on any run of whitespace and drops empties. |
| q9 | `3` | 0 + 1 + 2, then `break` at 3 before adding it. |
| q10 | `5` | The first value over 2 is 5. `return` leaves immediately. |
| q11 | `[(3, 3), (1, 2)]` | Pairs of (value, count), biggest count first. |
| q12 | `{"a": 2, "b": 1}` | The second "a" overwrites the first. Keys are unique. |
| q13 | `["fig", "pear", "apple"]` | Sorted by length: 3, 4, 5. |
| q14 | `None` | `.sort()` sorts in place and returns `None`. |
| q15 | `3` | a=0, b=1, c=2, d=3. |
