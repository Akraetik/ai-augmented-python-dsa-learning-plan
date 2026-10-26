"""
LAB 0.00 — Trace It: Predict the Output                     Tier: Warm-up
Lesson: 00.3 and 00.4

HOW THIS LAB WORKS
Each question shows a few lines of code. Do NOT run them yet.
Predict what gets printed. Type your answer into ANSWERS as a Python value.
  - a list:    [1, 2, 3]
  - a string:  "abc"
  - a number:  7
  - None:      None
Then run this file. It tells you which ones you got right (not what the answers are).

For any you miss: copy that code into a scratch file, run it, and figure out WHY.
The "why" is the lesson. Plain answers are in solutions/lab_00_trace_basics_answers.md.
"""

# q1
# nums = [5, 8, 2]
# for i, x in enumerate(nums):
#     nums[i] = x + i
# print(nums)

# q2
# s = "abcde"
# print(s[1:4][::-1])

# q3
# total = 0
# for i in range(2, 10, 3):
#     total += i
# print(total)

# q4
# nums = [1, 2, 3, 4]
# print(nums[1:3])

# q5
# x = [1, 2, 3]
# y = x
# y.append(4)
# print(len(x))

# q6
# print(17 // 5)

# q7
# print(-7 // 2)

# q8
# s = "  Hello   World  "
# print(s.split())

# q9
# total = 0
# for i in range(5):
#     if i == 3:
#         break
#     total += i
# print(total)

# q10
# def f(nums):
#     for x in nums:
#         if x > 2:
#             return x
#     return -1
# print(f([1, 5, 3]))

# q11
# from collections import Counter
# c = Counter([3, 1, 3, 2, 3, 1])
# print(c.most_common(2))

# q12
# d = {}
# for i, w in enumerate(["a", "b", "a"]):
#     d[w] = i
# print(d)

# q13
# print(sorted(["pear", "fig", "apple"], key=len))

# q14
# a = [3, 1, 2]
# b = a.sort()
# print(b)

# q15
# print(ord("d") - ord("a"))


# ---------- your answers (replace each ... ) ----------
ANSWERS = {
    "q1": ...,
    "q2": ...,
    "q3": ...,
    "q4": ...,
    "q5": ...,
    "q6": ...,
    "q7": ...,
    "q8": ...,
    "q9": ...,
    "q10": ...,
    "q11": ...,
    "q12": ...,
    "q13": ...,
    "q14": ...,
    "q15": ...,
}

# ---------- tests: don't edit below ----------
from _check import check_answers

KEY = {'q1': 'bfd747c2b391021b', 'q2': '692d6eb338c12406', 'q3': 'c5d43541e99c9b4a', 'q4': '32ad3fce1a51f19e', 'q5': 'f17c9766afecdc91', 'q6': '6836919c7852e090', 'q7': '765f0655178d3bcd', 'q8': '3a1c9ec6255efad0', 'q9': 'bc853de29ea2f137', 'q10': '1e84093fdbd9bb2e', 'q11': '1fec3488ac75407c', 'q12': '10b616e806006f92', 'q13': '3c1b919ad3738e9b', 'q14': '6373d70a0937fa77', 'q15': '6fef653435b81319'}
STUDY = {
    'q1': 'lessons/00.3-python-toolkit-1.md › Index vs value + enumerate',
    'q2': 'lessons/00.3-python-toolkit-1.md › Slicing (stop index is not included) and [::-1]',
    'q3': 'lessons/00.3-python-toolkit-1.md › Loops: range(start, stop, step)',
    'q4': 'lessons/00.3-python-toolkit-1.md › Slicing',
    'q5': "lessons/00.3-python-toolkit-1.md › Functions: a name points to a list, it doesn't copy it",
    'q6': 'lessons/00.4-python-toolkit-2.md › Numbers: // and %',
    'q7': 'lessons/00.4-python-toolkit-2.md › Numbers: // rounds DOWN',
    'q8': 'lessons/00.3-python-toolkit-1.md › String tools: split()',
    'q9': 'lessons/00.3-python-toolkit-1.md › break and continue',
    'q10': 'lessons/00.3-python-toolkit-1.md › Returning from inside a loop',
    'q11': 'lessons/00.4-python-toolkit-2.md › Counter and most_common',
    'q12': 'lessons/00.4-python-toolkit-2.md › Dicts: keys are unique, later values overwrite',
    'q13': 'lessons/00.4-python-toolkit-2.md › Sorting with key=',
    'q14': 'lessons/00.4-python-toolkit-2.md › Sorting: .sort() returns None',
    'q15': 'lessons/00.3-python-toolkit-1.md › Characters as numbers: ord()',
}
ENTRY = "ANSWERS"


def run_tests(answers):
    return check_answers(answers, KEY, title="trace predictions", study=STUDY)


if __name__ == "__main__":
    run_tests(ANSWERS)
