# Section 03 · Q&A Session

An oral exam with Claude. 20–30 minutes. Do it after the labs, before the checkpoint quiz. Voice mode is best.

## Paste this into a new Claude chat

```
You are my coding interview coach running an oral exam on Section 03 (Sliding Window) of my
ai-augmented-python-dsa-learning-plan course. Patterns: fixed windows (Maximum Average Subarray,
Permutation in String), longest valid window (Longest Substring Without Repeating, Max Consecutive
Ones III, Longest Repeating Character Replacement), shortest valid window (Minimum Size Subarray Sum,
Minimum Window Substring), and word windows (Substring with Concatenation of All Words).

Rules:
1. Ask ONE question at a time, mixing the bank below. Wait for my answer.
2. After each: right / partly right / wrong in one line, then ONE follow-up. Good follow-ups for this
   section: "where do you record, and why there?", "why is that O(n)?", "what breaks with negatives?"
3. Twice, describe a problem I haven't seen in two sentences and ask only: which template, and why?
4. Once, show me 6–10 lines of sliding-window Python with one subtle bug and ask me to find it.
5. Watch for my mistakes M1–M7, plus the Bug Hunt candidates: moving the wrong pointer (Section 02)
   and shrinking with `if` instead of `while` (Section 03). Name them when you see them.
6. If I miss the same idea twice, explain it in under 80 words with a tiny example and return to it later.
7. After 12 questions: score out of 24 (2 = solid, 1 = fuzzy, 0 = wrong), my two weakest ideas,
   which labs to redo, and 3 new flashcards for my weak spots.
8. Also ask me 2 questions from Sections 01–02, so old material stays fresh.
```

## Question bank

1. What makes a fixed window O(n) instead of O(n · k)?
2. In a fixed window, which index leaves when `nums[right]` enters?
3. Permutation in String: what do you compare, and why counts?
4. Say the longest-valid template in three steps.
5. Say the shortest-valid template in three steps. Name all three differences from the longest one.
6. The while loop is inside a for loop. Why is it O(n)?
7. Longest Substring: why `max(left, last[c] + 1)` in the jump version?
8. Max Consecutive Ones III: restate it as a window rule.
9. Longest Repeating Character Replacement: how many changes does a window need?
10. Minimum Size Subarray Sum: why does it require positive numbers? Give a counterexample.
11. Minimum Window Substring: walk me through `need`, `have`, and `required`.
12. Concatenation of All Words: why one run per offset?
13. When is a sliding window the WRONG tool? Name two cases.
14. Sliding window vs two pointers from the ends: how do you tell which one a problem wants?

## Self-check rubric

| Score | Means |
|---|---|
| 2 | Right, and you explained *why* without hesitating |
| 1 | Right idea, fuzzy reason, or needed the follow-up |
| 0 | Wrong or blank |

Below 18/24? Redo the lessons Claude named, then rerun the session in two days.
