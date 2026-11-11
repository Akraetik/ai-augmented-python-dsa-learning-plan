# Section 03 · Sliding Window Checkpoint — Answer Key

**1. B** — Everything in the middle stays. Add the new right item, remove the old left item. *Study: 3.1 Fixed-Size Windows › The idea.*

**2. B** — The window was right−k .. right−1. After the slide it's right−k+1 .. right, so right−k leaves. *Study: 3.1 Fixed-Size Windows › Worked example.*

**3. B** — About n windows, each summed in k steps. *Study: 3.1 Fixed-Size Windows › The idea (the slow way).*

**4. C** — A rearrangement has exactly the same letter counts. *Study: 3.1 Fixed-Size Windows › Fixed windows of counts.*

**5. B** — right − left + 1 = 5. Indexes 3, 4, 5, 6, 7. (M5) *Study: 3.2 Longest Valid Window › The template.*

**6. B** — The while loop fixes a broken window. Record once it's valid again. *Study: 3.2 Longest Valid Window › The template.*

**7. B** — In "abcdb", the repeat 'b' is 3 steps in. One step isn't enough. (Bug Hunt 3.09) *Study: 3.2 Longest Valid Window › The template (while, not if).*

**8. B** — Amortized: right moves n times, left moves at most n times. At most 2n steps. *Study: 3.2 Longest Valid Window › Why it's O(n).*

**9. B** — "ab" or "ba". The jump version needs max() so left never moves back. *Study: 3.2 Longest Valid Window › Longest Substring.*

**10. B** — You never flip anything. You just allow up to k zeros inside. *Study: 3.2 Longest Valid Window › Max Consecutive Ones III.*

**11. B** — Length 5 − most common count 3 = 2 changes needed. 2 > 1. *Study: 3.2 Longest Valid Window › Longest Repeating Character Replacement.*

**12. B** — While valid: record, then shrink to see if a shorter window still works. *Study: 3.3 Shortest Valid Window › The template.*

**13. C** — Any real answer must beat it with min(). 0 would win every time. *Study: 3.3 Shortest Valid Window › The template.*

**14. C** — The problem says 0. Check the no-answer case. (M6) *Study: 3.3 Shortest Valid Window › Minimum Size Subarray Sum.*

**15. B** — With negatives, shrinking can raise the sum. The window can't tell which way to move. *Study: 3.3 Shortest Valid Window › When sliding windows break.*

**16. B** — Only the moment a letter becomes satisfied. Extra copies don't count again. *Study: 3.3 Shortest Valid Window › Minimum Window Substring.*

**17. B** — You need both to slice the answer at the end. *Study: 3.3 Shortest Valid Window › Minimum Window Substring.*

**18. B** — One per offset 0, 1, 2, 3. Together they cover every start. *Study: 3.4 Word Windows › The catch: where do the pieces start?.*

**19. B** — No valid window can contain that piece. *Study: 3.4 Word Windows › Inside one run.*

**20. B** — Shrinking may not lower the sum. Use prefix sums (Section 05) or other tools. *Study: Review: review/TRIGGERS.md.*

**21. A** — Every window of size k. (A deque makes the max O(1) per slide; that's a later trick.) *Study: Review: review/TRIGGERS.md.*

**22. B** — A pair from anywhere, not a contiguous run. Windows are for runs of items next to each other. *Study: Review: review/TRIGGERS.md.*


## If you missed a topic

- **Fixed-size windows (3.1):** Lesson 3.1. Redo labs 01 and 02.
- **Longest valid window (3.2):** Lesson 3.2. Redo labs 03, 04, 05 and the Bug Hunt (09).
- **Shortest valid window (3.3):** Lesson 3.3. Redo lab 06, then trace lab 07 by hand.
- **Word windows (3.4):** Lesson 3.4. Re-draw the three offsets, then redo lab 08.
- **Picking the pattern:** Read review/TRIGGERS.md. Cover the right columns and name each pattern.
