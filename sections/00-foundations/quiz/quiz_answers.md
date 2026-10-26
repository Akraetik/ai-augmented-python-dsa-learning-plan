# Section 00 · Diagnostic and Checkpoint — Answer Key

**1. B** — Graders read the return value. A function with no `return` gives back `None`. *Study: 00.1 How Coding Tests Work › Return, don't print.*

**2. B** — `-> None` plus "in place" means: change the input list itself. The grader inspects that list. *Study: 00.1 How Coding Tests Work › Return, don't print (in-place problems).*

**3. C** — All pairs of 100,000 items is about 5 billion steps. Python manages tens of millions per second. *Study: 00.2 Big-O › Read the constraints, know your target.*

**4. B** — `i` is halved each pass, so the loop runs about log2(n) times. *Study: 00.2 Big-O › The halving loop: O(log n).*

**5. C** — `-x in nums` scans the list each time. That's a hidden loop inside the visible loop. *Study: 00.2 Big-O › Hidden loops in Python (`in` on a list).*

**6. D** — `pop(0)` shifts every remaining item left. Use `collections.deque.popleft()` instead. *Study: 00.2 Big-O › Hidden loops in Python (pop(0)).*

**7. B** — O(n log n) + O(n). Keep the biggest term. *Study: 00.2 Big-O › Drop constants and small terms.*

**8. A** — Slices stop before the stop index. `nums[-1]` is the last item. *Study: 00.3 Python Toolkit 1 › Slicing.*

**9. B** — A plain `for` gives values. Use `range(len(nums))` for indexes or `enumerate` for both (Mistake M1). *Study: 00.3 Python Toolkit 1 › Index vs value.*

**10. B** — `b = a` doesn't copy. Both names point to the same list. *Study: 00.3 Python Toolkit 1 › Functions (b = a doesn't copy).*

**11. C** — Multiplying the outer list copies references to ONE row. The comprehension makes three separate rows. *Study: 00.3 Python Toolkit 1 › Lists of lists: the trap.*

**12. B** — `split()` with no argument splits on any run of whitespace and drops empty pieces. *Study: 00.3 Python Toolkit 1 › String tools: split().*

**13. B** — Strings are immutable, so `+=` makes a new string every pass. One `join` at the end is linear. *Study: 00.3 Python Toolkit 1 › Building a string: use a list.*

**14. A** — a=0, b=1, c=2, d=3, e=4. This maps letters to indexes 0–25. *Study: 00.3 Python Toolkit 1 › Characters as numbers.*

**15. B** — Mistake M7: a True answer usually waits until every item is checked. Return False early on a bad one. *Study: 00.3 Python Toolkit 1 › Returning from inside a loop (M7).*

**16. B** — Mistake M4: `left + 1` computes a value and throws it away. `left` never changes. It needs `left += 1`. *Study: 00.3 Python Toolkit 1 › while loops (M4).*

**17. B** — Start 2, step 3, stop before 11: 2, 5, 8. *Study: 00.3 Python Toolkit 1 › for loops: range().*

**18. B** — Set membership is O(1). List membership is O(n). *Study: 00.4 Python Toolkit 2 › Sets.*

**19. B** — `.get(ch, 0)` returns 0 for a new key, so no KeyError. 'a' appears twice. *Study: 00.4 Python Toolkit 2 › Dicts: pattern counting.*

**20. B** — Standing on x, you look up `target - x`. You need that value's index, so map value -> index. *Study: 00.4 Python Toolkit 2 › Dicts: remember where you saw it.*

**21. B** — Set items and dict keys must be hashable (immutable). Use a tuple `(1, 2)`. *Study: 00.4 Python Toolkit 2 › Tuples and unpacking (hashable keys).*

**22. B** — Sets lose counts: 'aab' and 'abb' have the same set. Counter keeps counts. *Study: 00.4 Python Toolkit 2 › Counter.*

**23. C** — `.sort()` sorts in place and returns None. Use `sorted(...)` to get a new list. *Study: 00.4 Python Toolkit 2 › Sorting (.sort() returns None).*

**24. B** — deque removes from either end in O(1). The others are O(n) each time. *Study: 00.4 Python Toolkit 2 › deque.*

**25. A** — Mistake M5: on the last i, `i + 1` is past the end. Stop one early. *Study: 00.5 Routine and Debugging › Reading error messages (IndexError).*

**26. B** — Understand first. Writing `RETURNS: ___` also guards against Mistake M6. *Study: 00.5 Routine and Debugging › The routine, with a real example.*


## If you missed a topic

- **How tests are graded:** Lesson 00.1. Re-read 'Return, don't print' and 'Hidden tests'.
- **Big-O:** Lesson 00.2, the ladder and the constraints table. Redo `lab_01_bigo_spotter.py` and `lab_10_speed_trap.py`.
- **Lists and indexing:** Lesson 00.3, Lists. Redo `lab_00_trace_basics.py` and `lab_04_reverse_in_place.py`.
- **Strings:** Lesson 00.3, Strings. Practice `split`, `join`, `ord`, slicing in a scratch file.
- **Loops and returns:** Lesson 00.3, Loops. Redo `lab_07_max_consecutive_ones.py`. Check MISTAKES M4, M5, M7.
- **Dicts and sets:** Lesson 00.4. Redo `lab_05_contains_duplicate.py` and `lab_09_two_sum.py`.
- **collections and sorting:** Lesson 00.4, collections and Sorting. Redo `lab_08_valid_anagram.py` with Counter.
- **Routine and debugging:** Lesson 00.5. Redo `lab_11_bug_hunt.py` and trace two labs on paper.
