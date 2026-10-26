# Section 01 · Q&A Session

An oral exam with Claude. 30–40 minutes. Do it after the labs, before the checkpoint quiz.
Use voice mode if you can. Live interviews are spoken.

## Paste this into a new Claude chat

```
You are my coding interview coach running an oral exam on Section 01 (Array / String) of my
ai-augmented-python-dsa-learning-plan course. The patterns: read/write pointers, counting and Boyer–Moore voting,
modulo and the three-reversal rotation, best-so-far scans, reach/greedy (Jump Game I/II, Gas Station),
prefix/suffix passes (Product Except Self, Trapping Rain Water, Candy), list+dict design
(RandomizedSet), and string processing (last word, common prefix, reverse words, substring search,
Roman numerals, zigzag, text justification).

Rules:
1. Ask ONE question at a time, mixing the three kinds in the bank below. Wait for my answer.
2. After each answer: right / partly right / wrong in one line, then ONE follow-up that pushes deeper
   ("why does that work?", "what if the input were ___?", "what's the Big-O and why?"). No lectures.
3. At least twice, give me a problem I haven't seen that uses one of these patterns (describe it in two
   sentences) and ask me only: which pattern, and why? Don't let me code it.
4. At least once, show me 6–10 lines of Python with one subtle bug and ask me to find it.
5. Watch for my known mistakes M1–M7 (index vs value, wrong loop, meaningless check, unsaved
   calculation, off-by-one, ignoring return type, returning True too early). Name them by ID when you see them.
6. If I miss the same idea twice, explain it in under 80 words with a tiny example, and come back to it later.
7. After 15 questions: score out of 30 (2 = solid, 1 = fuzzy, 0 = wrong), my two weakest patterns,
   which labs to redo, and 4 new flashcards (front / back) aimed at my weak spots.
```

## Question bank

**Explain it**
1. Walk me through the read/write pointer pattern. Why can `write` never pass `read`?
2. In Remove Duplicates II, why compare with `nums[write - 2]` and not `nums[read - 2]`?
3. Why does Merge Sorted Array fill from the back?
4. Explain Boyer–Moore voting in plain words. What guarantee does it rely on?
5. Why does H-Index sort descending and compare citations to paper number?
6. Why reduce `k %= n` in Rotate Array? Why do three reversals work?
7. In Best Time to Buy and Sell, why do you track the lowest price so far and not the highest?
8. Why is "add every positive daily difference" correct for Stock II?
9. In Jump Game, what does `reach` mean, exactly? When are you stuck?
10. In Jump Game II, what are the "rings," and when do you count a jump?
11. In Gas Station, why can you skip every station between the old start and where you ran dry?
12. In Product Except Self, why is division a bad idea? Walk me through the two passes.
13. Trapping Rain Water: what limits the water above one bar?
14. Candy: why two sweeps? Why `max` in the second one?
15. RandomizedSet: why a list AND a dict? Walk me through `remove`.
16. Roman to Integer: what's the subtract rule? What's special about the last symbol?
17. Integer to Roman: why does greedy work only if 900, 400, 90, 40, 9, 4 are in the table?
18. Zigzag: why simulate instead of finding a formula? What breaks at one row?

**Name the pattern**
19. "Return the number of items after removing every negative number, in place." Pattern?
20. "Find the biggest drop: `a[i] - a[j]` where `i < j`." Pattern? What do you track?
21. "For each day, how many days until a warmer one?" — Is this a prefix pass? (Trick: it's a stack problem, Section 07.)
22. "For each index, the sum of everything except itself." Pattern? Can you use division here?
23. "Shift a circular list left by k." Pattern? What's different from rotating right?

**Big-O check**
24. What's the Big-O of `sorted(nums)[len(nums) // 2]` for Majority Element? Why is it still a decent answer?
25. A Rotate Array solution pops from the end and inserts at the front, k times. Big-O? Why did it fail the speed test?
26. Your Longest Common Prefix compares every pair of words. Big-O? Better?

## Self-check rubric

| Score | Means |
|---|---|
| 2 | Right, and you explained *why* without hesitating |
| 1 | Right idea, fuzzy reason, or needed the follow-up |
| 0 | Wrong or blank |

Below 22/30? Redo the lessons Claude named, then rerun the session in two days with a fresh chat.
