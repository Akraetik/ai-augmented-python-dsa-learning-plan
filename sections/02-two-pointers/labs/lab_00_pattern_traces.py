"""
LAB 2.00 — Pattern Traces                                    Tier: Warm-up
Do each question right after its lesson. Trace on paper, write the result as a Python value, run the file.
It says which you got right, not what the answers are. Each miss prints where to study.
Answers with explanations: solutions/lab_00_pattern_traces_answers.md
"""

# t1 (Lesson 2.1) — opposite ends
# items has 6 elements. With left, right = 0, 5 and `while left < right:` moving BOTH inward each step,
# list every [left, right] pair the loop looks at, in order. Example format: [[0, 5], ...]

# t2 (Lesson 2.2) — same direction
# Is "bd" a subsequence of "abcde"? (True / False)

# t3, t4 (Lesson 2.1) — Two Sum II
# numbers = [1, 3, 4, 8], target = 7. Run the two-pointer method.
# t3: what does it return? (1-indexed positions, as a list)
# t4: how many times does the while loop body run, counting the step that finds the answer?

# t5 (Lesson 2.3) — Container With Most Water
# heights = [4, 1, 1, 1, 4]. Which pair of indexes [i, j] holds the most water?

# t6 (Lesson 2.3)
# heights = [1, 2, 1]. What is the biggest area?

# t7 (Lesson 2.4) — 3Sum
# What does 3Sum return for [-2, 0, 1, 1, 2]? Sort each triple and sort the list of triples.

# t8 (Lesson 2.4)
# How many unique triples does 3Sum find in [-1, 0, 1, 2, -1, -4]?


ANSWERS = {
    "t1": ...,
    "t2": ...,
    "t3": ...,
    "t4": ...,
    "t5": ...,
    "t6": ...,
    "t7": ...,
    "t8": ...,
}

# ---------- tests: don't edit below ----------
from _check import check_answers

KEY = {'t1': '45c1324829beb981', 't2': 'd9aa0dbf2477426d', 't3': '590e3b4793667b8a', 't4': 'a9ab08894817583f', 't5': 'e9ca29bc6bc84df9', 't6': '3969a2ebfb05ab9b', 't7': '5337941afcf8ffb9', 't8': '063df4cd50cbf527'}
STUDY = {
    't1': 'lessons/2.1-opposite-ends.md › The idea (the skeleton loop)',
    't2': 'lessons/2.2-same-direction.md › Is Subsequence (the slow pointer moves only on a match)',
    't3': 'lessons/2.1-opposite-ends.md › Use 2 — sorted pairs (and the answer is 1-indexed)',
    't4': 'lessons/2.1-opposite-ends.md › Use 2 — trace the sum: too big → right, too small → left',
    't5': 'lessons/2.3-shrink-the-weaker-side.md › area = width × shorter line',
    't6': 'lessons/2.3-shrink-the-weaker-side.md › area = width × shorter line',
    't7': 'lessons/2.4-sort-then-two-pointers.md › Turn three into "one + two"',
    't8': 'lessons/2.4-sort-then-two-pointers.md › The hard part: no duplicate triples',
}
ENTRY = "ANSWERS"


def run_tests(answers):
    return check_answers(answers, KEY, title="pattern traces", study=STUDY)


if __name__ == "__main__":
    run_tests(ANSWERS)
