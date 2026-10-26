# Section 02 · Two Pointers Checkpoint — Answer Key

**1. B** — Every iteration moves at least one pointer inward. At most n moves in total. *Study: 2.1 Opposite Ends › The idea.*

**2. B** — Only moving left can bring in a bigger number. *Study: 2.1 Opposite Ends › Use 2 — sorted pairs.*

**3. B** — If the biggest possible partner fails, no partner works for numbers[left]. *Study: 2.1 Opposite Ends › Use 2 (the one-sentence proof).*

**4. B** — The problem asks for 1-indexed positions. Mistake M6: read the return spec. *Study: 2.1 Opposite Ends › Use 2 (1-indexed answer).*

**5. C** — Nothing is alphanumeric, so the skip loop keeps going off the end. Guard every inner loop with `left < right`. *Study: 2.1 Opposite Ends › Use 1 — symmetry checks.*

**6. B** — |−6| > |5|. The biggest square is at one of the ends. *Study: 2.1 Opposite Ends › Use 3 — fill from the biggest end.*

**7. B** — j walks t every step. i (in s) moves only on a match. *Study: 2.2 Same Direction › Is Subsequence.*

**8. B** — After matching 'e' at index 4, there's no 'c' left. Order matters. *Study: 2.2 Same Direction › Is Subsequence.*

**9. A** — Delete everything from t. Zero characters to match means i == len(s) right away. *Study: 2.2 Same Direction › Edge cases.*

**10. A** — Width 5 × shorter line 6 = 30. *Study: 2.3 Shrink the Weaker Side › The problem (area formula).*

**11. B** — The short line caps every narrower container that keeps it. It's finished. Move it. *Study: 2.3 Shrink the Weaker Side › Two pointers: start wide.*

**12. B** — Same cap, less width: area can only fall. *Study: 2.3 Shrink the Weaker Side › Two pointers (the proof).*

**13. B** — Fixing one number turns 3Sum into a sorted pair search. *Study: 2.4 Sort First › Turn three into one + two.*

**14. B** — Skipping the LATER copies keeps the first one, which can still pair with the second. *Study: 2.4 Sort First › The hard part: no duplicate triples.*

**15. B** — Otherwise the same triple is recorded again. *Study: 2.4 Sort First › The hard part (after a match).*

**16. B** — Three positives can't sum to 0. *Study: 2.4 Sort First › An early exit.*

**17. B** — n fixed values × an O(n) pair scan. The sort is smaller. *Study: 2.4 Sort First › Turn three into one + two (cost).*

**18. A** — Left's own max is exact (3), and the right side has a taller bar, so the level at left is 3. *Study: 2.5 Water with Two Pointers › The key insight.*

**19. B** — No max_left / max_right lists. Same O(n) time. *Study: 2.5 Water with Two Pointers › Where we left it.*

**20. A** — Sorted + pair condition. If nums[l] + nums[r] < k, every pair (l, l+1..r) works: add r − l, move left. *Study: Review: review/TRIGGERS.md.*

**21. A** — Walk both lists forward, take the smaller head each step. O(m + n). *Study: Review: review/TRIGGERS.md.*

**22. A** — LeetCode 680. Same two pointers, with one extra check when the characters differ. *Study: Review: review/TRIGGERS.md.*


## If you missed a topic

- **Opposite ends (2.1):** Lesson 2.1. Redo labs 01, 03, 04 and the Bug Hunt (09).
- **Same direction (2.2):** Lesson 2.2. Redo lab 02.
- **Shrink the weaker side (2.3):** Lesson 2.3. Redo lab 05 and say the proof out loud.
- **Sort + two pointers / 3Sum (2.4):** Lesson 2.4. Redo labs 06 and 08. Trace the duplicate skips by hand.
- **O(1)-space water (2.5):** Lesson 2.5. Re-trace the table, then redo lab 07.
- **Picking the pattern:** Read review/TRIGGERS.md. Cover the right columns and name each pattern.
