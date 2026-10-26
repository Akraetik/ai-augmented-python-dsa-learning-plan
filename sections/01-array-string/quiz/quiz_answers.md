# Section 01 · Array / String Checkpoint — Answer Key

**1. B** — `write` marks the next slot for a kept item. It only moves after a keep. *Study: 1.1 Write Pointer › The idea: two pointers going the same way.*

**2. B** — Keeps the first 1, skips two 1s, keeps the 2. k = 2. *Study: 1.1 Write Pointer › The keep rule changes (Remove Duplicates).*

**3. B** — Look two KEPT slots back. `read - 2` breaks after earlier overwrites change what sits behind read. *Study: 1.1 Write Pointer › The keep rule changes (Remove Duplicates II).*

**4. B** — Filling from the front would overwrite nums1 values before you read them. *Study: 1.1 Write Pointer › A different direction: fill from the back.*

**5. B** — Rebinding the local name doesn't touch the caller's list. Use `nums[:] = new_list` or edit by index. *Study: 1.1 Write Pointer › Common mistakes (nums = new_list).*

**6. C** — 5 (1), 1 (0), 5 (1), 2 (0), 5 (1). Candidate 5. *Study: 1.2 Counting and Voting › Way 3: the voting trick.*

**7. B** — Cancellation only proves something when one value outnumbers all the others combined. *Study: 1.2 Counting and Voting › Way 3 (why the guarantee matters).*

**8. B** — Sorted desc: paper 4 has 4 ≥ 4 ✓, paper 5 has 3 ≥ 5 ✗. h = 4. *Study: 1.2 Counting and Voting › H-Index: sort, then read the picture.*

**9. C** — `k %= n` → 10 % 7 = 3. Rotating by n changes nothing. *Study: 1.3 Index Math and Reversal › Tool 1: modulo (reduce k first).*

**10. B** — Reversing all brings the last k to the front (backward); then fix each block's order. Option A rotates LEFT by k. Trace it to see. *Study: 1.3 Index Math and Reversal › Tool 2: the reversal trick.*

**11. B** — Every insert at the front shifts the whole list. *Study: 1.3 Index Math and Reversal › Three ways to solve Rotate Array.*

**12. A** — Best is buy 4, sell 9 = 5. Buying at 1 later gives only 5 too (1 → 6). Max 5. *Study: 1.4 Greedy Scans › Worked example: the biggest jump forward.*

**13. B** — At each day, best sale today = price − lowest so far. *Study: 1.4 Greedy Scans › The idea.*

**14. B** — Gains: 1→3 = 2, 2→5 = 3. Total 5. *Study: 1.4 Greedy Scans › Lab 09: many trades allowed.*

**15. B** — reach after index 0 is 2. Indexes 1 and 2 add nothing. Index 3 > reach. Stuck. *Study: 1.5 Reach and Greedy › The idea: track how far you could get.*

**16. B** — Reaching the ring end means you must jump to move on. The new ring end becomes `farthest`. *Study: 1.5 Reach and Greedy › Jump Game II: counted in levels.*

**17. C** — No station from 2 to 6 can work (each would start with less fuel than you had). Next try is 7. *Study: 1.5 Reach and Greedy › Gas Station: Fact 2.*

**18. B** — Not enough fuel overall means no start works. *Study: 1.5 Reach and Greedy › Gas Station: Fact 1.*

**19. B** — Empty product is 1. Then 2. Then 2 × 3 = 6. *Study: 1.6 Prefix and Suffix › Product of Array Except Self.*

**20. B** — Division by zero crashes, and one or two zeros need special handling. Prefix × suffix needs none. *Study: 1.6 Prefix and Suffix › Product of Array Except Self (why no division).*

**21. B** — Water spills over the shorter side. *Study: 1.6 Prefix and Suffix › Trapping Rain Water.*

**22. A** — Plain assignment could lower a value sweep one required. max keeps both rules true. *Study: 1.6 Prefix and Suffix › Candy.*

**23. B** — Only the end of a list can be removed in O(1). Moving the last value in keeps the list dense. *Study: 1.7 List + Dict Design › The hard part: removing from the middle in O(1).*

**24. B** — random.choice needs indexable data. A list gives that. *Study: 1.7 List + Dict Design › Why one structure isn't enough.*

**25. B** — Compare column by column across every word. Looping over words first is Mistake M2. *Study: 1.8 String Processing › Skill 2: compare column by column.*

**26. C** — n − m = 6. `range(n − m + 1)` covers 0 through 6. *Study: 1.8 String Processing › Skill 4: matching a pattern inside a string.*

**27. B** — X before a bigger C subtracts: 100 − 10. *Study: 1.8 String Processing › Skill 5: lookup tables.*

**28. B** — One row means no zigzag. Without this check, row 0 is also the bottom row and the step logic pushes past the last row. *Study: 1.8 String Processing › Skill 6: simulate, then look for the pattern.*

**29. B** — divmod(7, 3) = (2, 1). The first 1 gap gets an extra: 3, 2, 2. *Study: 1.8 String Processing › Skill 7: careful bookkeeping.*

**30. B** — In place + return k + keep order = write pointer. *Study: 1.1 Write Pointer › Pattern trigger.*

**31. A** — One right-to-left sweep with a running max. O(n). *Study: 1.6 Prefix and Suffix › Worked example: biggest number to the left (mirror it).*

**32. B** — Sorting loses the i < j order. Track the min seen so far. *Study: 1.4 Greedy Scans › The idea (order matters, so no sorting).*


## If you missed a topic

- **Read/write pointers (1.1):** Lesson 1.1. Redo labs 03, 04, and the Bug Hunt (25) from a blank file.
- **Counting and voting (1.2):** Lesson 1.2. Redo lab 05 three ways, then lab 06.
- **Index math and rotation (1.3):** Lesson 1.3. Redo lab 07 both ways.
- **Best-so-far scans (1.4):** Lesson 1.4. Redo labs 08 and 09 from memory.
- **Reach and greedy (1.5):** Lesson 1.5. Trace Jump Game I and II on paper with all variables. Redo labs 10–12.
- **Prefix and suffix passes (1.6):** Lesson 1.6. Redo lab 13, then lab 14. Draw the max_left / max_right rows by hand.
- **List + dict design (1.7):** Lesson 1.7. Redo lab 16, tracing remove() on the last element.
- **String processing (1.8):** Lesson 1.8. Redo labs 18, 20, 21, 23.
- **Picking the pattern:** Re-read the 'Pattern trigger' box at the end of every lesson. Add any you missed as Anki cards.
