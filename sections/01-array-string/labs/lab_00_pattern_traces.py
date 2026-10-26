"""
LAB 1.00 — Pattern Traces                                    Tier: Warm-up
Do this after reading lessons 1.1–1.8 (or do each question right after its lesson).

Each question runs a pattern from the lessons on a NEW input. Trace it on paper. Write the result as a
Python value. Then run this file. It says which you got right, not what the answers are.
Answers with explanations: solutions/lab_00_pattern_traces_answers.md
"""

# t1, t2 (Lesson 1.1) — the write pointer
# def keep_evens(nums):
#     write = 0
#     for read in range(len(nums)):
#         if nums[read] % 2 == 0:
#             nums[write] = nums[read]
#             write += 1
#     return write
#
# nums = [4, 1, 6, 6, 3]
# k = keep_evens(nums)
# t1: what is k?
# t2: what is nums after the call (the WHOLE list)?

# t3 (Lesson 1.2) — Boyer–Moore voting
# Run the voting algorithm on [3, 3, 4, 2, 4, 4, 2, 4, 4]. What is the final candidate?

# t4 (Lesson 1.3) — modulo
# Rotating right by k = 4 in a list of length n = 7. The item at index 5 moves to which index?

# t5 (Lesson 1.4) — best-so-far scan
# Run biggest_rise (best nums[j] - nums[i] with i < j, else 0) on [9, 4, 6, 1, 3]. Result?

# t6 (Lesson 1.6) — record, then include
# def max_to_left(nums):
#     out = [0] * len(nums)
#     best = float("-inf")
#     for i in range(len(nums)):
#         out[i] = best
#         best = max(best, nums[i])
#     return out
# What does max_to_left([2, 5, 1, 3]) return? (write float("-inf") where needed)

# t7 (Lesson 1.6) — left products
# For nums = [2, 3, 4], what is the list of "product of everything strictly LEFT of i"?

# t8 (Lesson 1.5) — reach
# Jump Game on [1, 0, 2]: can you reach the last index? (True / False)

# t9 (Lesson 1.8) — zigzag
# Zigzag "ABCDE" with numRows = 2, then read row by row. Result?

# t10 (Lesson 1.8) — Roman to integer
# "XIV" = ?


ANSWERS = {
    "t1": ...,
    "t2": ...,
    "t3": ...,
    "t4": ...,
    "t5": ...,
    "t6": ...,
    "t7": ...,
    "t8": ...,
    "t9": ...,
    "t10": ...,
}

# ---------- tests: don't edit below ----------
from _check import check_answers

KEY = {'t1': '4f86d14861b96c5d', 't2': 'fe327fd4fbccd015', 't3': 'bd672d146a606522', 't4': 'c93883b7311ca97d', 't5': '98dd4c214d410398', 't6': '824a2d29dd9f3d95', 't7': '5a39c35d5a73e6ac', 't8': 'c8bace05ebff66bf', 't9': 'ce02444e73a40726', 't10': '61779fed0157d071'}
STUDY = {
    't1': 'lessons/1.1-in-place-and-the-write-pointer.md › Worked example: keep only the even numbers',
    't2': 'lessons/1.1-in-place-and-the-write-pointer.md › Trace it (the tail is leftover junk)',
    't3': 'lessons/1.2-counting-and-voting.md › Way 3: the voting trick',
    't4': 'lessons/1.3-index-math-and-reversal.md › Tool 1: modulo wraps an index',
    't5': 'lessons/1.4-greedy-scans.md › Worked example: the biggest jump forward',
    't6': 'lessons/1.6-prefix-and-suffix-passes.md › Worked example: record first, then include yourself',
    't7': 'lessons/1.6-prefix-and-suffix-passes.md › Product of Array Except Self (left product row)',
    't8': 'lessons/1.5-reach-and-greedy-choice.md › The idea: track how far you could get',
    't9': 'lessons/1.8-string-processing.md › Skill 6: simulate the zigzag',
    't10': 'lessons/1.8-string-processing.md › Skill 5: lookup tables (Roman → integer)',
}
ENTRY = "ANSWERS"


def run_tests(answers):
    return check_answers(answers, KEY, title="pattern traces", study=STUDY)


if __name__ == "__main__":
    run_tests(ANSWERS)
