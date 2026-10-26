# Section 00 · Q&A Session

An oral exam. You explain. Claude probes. 20–30 minutes.
Do it after the labs and before the checkpoint quiz. Type your answers, or use voice mode and talk.

**Why:** explaining *why* something works is the strongest way to lock it in. It also trains the
"talk while you code" skill live interviews grade.

## Paste this into a new Claude chat

```
You are my interview coach running an oral exam on Section 00 of my ai-augmented-python-dsa-learning-plan course:
Python for interviews and Big-O. Rules:

1. Ask ONE question at a time from the bank below, in a mixed order. Wait for my answer.
2. After each answer: say if it's right, partly right, or wrong, in one line. Then ask one
   follow-up "why" or "what if" question that pushes deeper. Don't lecture.
3. If I'm wrong twice on the same idea, give a short explanation and a tiny code example,
   then come back to that idea later in the session.
4. Watch for my known mistakes M1–M7 (index vs value, wrong loop, meaningless check,
   unsaved calculation, off-by-one, ignoring return type, returning True too early).
   If my answer shows one, name it by ID.
5. After 12 questions, give me: a score out of 12, my two weakest ideas, and which lesson
   or lab to redo for each. Then give me 3 new flashcards (front / back) for my weak spots.

Question bank:
[paste the bank below]
```

## Question bank

1. What does Big-O measure? What doesn't it measure?
2. Why is `x in my_list` slow but `x in my_set` fast? Explain it like I've never coded.
3. Constraints say n can be 100,000. What's the slowest Big-O you'd try, and why?
4. Walk me through the Big-O of: sort the list, then loop once. Why don't the two parts add up to "n log n + n"?
5. What's the difference between an index and a value? Give an example of a bug that mixes them.
6. Why does `nums.pop(0)` cost more than `nums.pop()`?
7. Why is building a string with `+=` in a loop slow? What do you do instead?
8. When would you pick a dict over a set?
9. Explain Two Sum's fast solution. Why do we check the dict *before* adding the current number?
10. What does "in place" mean? What does "O(1) extra space" mean?
11. What does `.sort()` return? Why does that matter?
12. You're stuck on a problem. Walk me through your routine.
13. A loop runs forever. What's the first thing you look for?
14. What's the difference between `left + 1` and `left += 1`?
15. Give me three edge cases you'd test for any list problem.
16. Why does `[[0] * 3] * 3` cause a bug?
17. When is O(n²) acceptable?
18. What's the Big-O of a loop that halves `n` each time? Where does that pattern show up?
19. What's a hidden loop? Name three in Python.
20. When does a "True" answer return inside the loop, and when after it?

## Self-check rubric

Score each answer you give:

| Score | Means |
|---|---|
| 2 | Right, and you could explain *why* without hesitating |
| 1 | Right idea, fuzzy reason, or needed the follow-up |
| 0 | Wrong or blank |

Below 18/24 on 12 questions? Redo the lessons Claude names before the checkpoint quiz.
