# Section 02 · Q&A Session

An oral exam with Claude. 20–30 minutes. Do it after the labs, before the checkpoint quiz. Voice mode is best.

## Paste this into a new Claude chat

```
You are my coding interview coach running an oral exam on Section 02 (Two Pointers) of my
ai-augmented-python-dsa-learning-plan course. Patterns: opposite ends (Valid Palindrome, Two Sum II, Squares of a Sorted
Array), same direction (Is Subsequence), shrink the weaker side (Container With Most Water),
sort + two pointers (3Sum, 3Sum Closest), and O(1)-space Trapping Rain Water.

Rules:
1. Ask ONE question at a time, mixing the bank below. Wait for my answer.
2. After each: right / partly right / wrong in one line, then ONE follow-up. The best follow-up for
   this section is "why is it safe to move THAT pointer?" Ask it often.
3. Twice, describe a problem I haven't seen in two sentences and ask only: which pattern, and why?
4. Once, show me 6–10 lines of two-pointer Python with one subtle bug and ask me to find it.
5. Watch for my mistakes M1–M7, plus the new one from lab 2.09: moving the wrong pointer.
   Name them when you see them.
6. If I miss the same idea twice, explain it in under 80 words with a tiny example and return to it later.
7. After 12 questions: score out of 24 (2 = solid, 1 = fuzzy, 0 = wrong), my two weakest ideas,
   which labs to redo, and 3 new flashcards for my weak spots.
8. Also ask me 2 questions from Section 01 (Array/String), so old material stays fresh.
```

## Question bank

1. What makes an opposite-ends loop O(n)?
2. Two Sum II: walk me through why each pointer move is safe.
3. Why does Two Sum II not need a dict, when Two Sum (Section 00) did?
4. Valid Palindrome: why do the skip loops need `left < right`?
5. Squares of a Sorted Array: where are the biggest squares, and why fill from the back?
6. Is Subsequence: which pointer is fast, which is slow, and why is greedy matching safe?
7. Container With Most Water: prove that moving the shorter line can't lose the answer.
8. What do Container and two-pointer Trapping Rain Water have in common?
9. 3Sum: why sort? What's the Big-O, and why can't you easily do better?
10. 3Sum: name the three duplicate skips. Why `i - 1` and not `i + 1`?
11. 3Sum Closest: what changes from 3Sum, and what doesn't?
12. Trapping Rain Water with two pointers: which side do you process, and why is its water level known?
13. When do you use `left < right` vs `left <= right`?
14. Name a problem where two pointers would be WRONG, and why. (Hint: unsorted pair sums. Use a dict.)

## Self-check rubric

| Score | Means |
|---|---|
| 2 | Right, and you explained *why* without hesitating |
| 1 | Right idea, fuzzy reason, or needed the follow-up |
| 0 | Wrong or blank |

Below 18/24? Redo the lessons Claude named, then rerun the session in two days.
