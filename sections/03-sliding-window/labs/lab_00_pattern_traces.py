"""
LAB 3.00 — Pattern Traces                                    Tier: Warm-up
Do each question right after its lesson. Trace on paper, write the result as a Python value, run the file.
It says which you got right, not what the answers are. Each miss prints where to study.
Answers with explanations: solutions/lab_00_pattern_traces_answers.md
"""

# t1 (Lesson 3.1) — fixed window
# nums = [2, 1, 5, 1, 3, 2], k = 3. List the sum of every window of size 3, left to right.

# t2 (Lesson 3.1)
# What is the biggest of those sums?

# t3 (Lesson 3.2) — longest valid
# Length of the longest substring of "dvdf" with no repeated letter?

# t4 (Lesson 3.2)
# A window runs from left = 2 to right = 5. How many items are in it?

# t5 (Lesson 3.2)
# Max Consecutive Ones III: nums = [1, 0, 1, 1, 0, 1], k = 1. Longest run of 1s after flipping at most one 0?

# t6 (Lesson 3.3) — shortest valid
# Minimum Size Subarray Sum: nums = [2, 1, 5, 2, 8], target = 7. Length of the shortest run with sum >= 7?

# t7 (Lesson 3.3)
# Minimum Window Substring: s = "XAYBZACB", t = "ABC". What substring is returned?

# t8 (Lesson 3.4) — word windows
# s = "catdogcatcat", words = ["cat", "dog"]. Every start index where all the words appear back to back?


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

KEY = {'t1': 'afedee7219eb66f1', 't2': '4afe58dc26a55bfb', 't3': 'cf3c9b67dbeebd3e', 't4': 'e265cb99ba635c99', 't5': 'bd3bc55633d02548', 't6': 'c6657b5f64c1123b', 't7': 'dce7e1031ff83636', 't8': '9da1eef44ea92ec1'}
STUDY = {
    't1': 'lessons/3.1-fixed-size-window.md › The idea (one enters, one leaves)',
    't2': 'lessons/3.1-fixed-size-window.md › Worked example: the biggest sum of any k items',
    't3': 'lessons/3.2-longest-valid-window.md › Longest Substring Without Repeating Characters',
    't4': 'lessons/3.2-longest-valid-window.md › The template (right - left + 1)',
    't5': 'lessons/3.2-longest-valid-window.md › Max Consecutive Ones III (at most k zeros)',
    't6': 'lessons/3.3-shortest-valid-window.md › Minimum Size Subarray Sum',
    't7': 'lessons/3.3-shortest-valid-window.md › Minimum Window Substring',
    't8': 'lessons/3.4-word-windows.md › The catch: where do the pieces start?',
}
ENTRY = "ANSWERS"


def run_tests(answers):
    return check_answers(answers, KEY, title="pattern traces", study=STUDY)


if __name__ == "__main__":
    run_tests(ANSWERS)
