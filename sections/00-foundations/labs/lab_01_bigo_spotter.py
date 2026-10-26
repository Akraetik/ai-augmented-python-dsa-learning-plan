"""
LAB 0.01 — Big-O Spotter                                     Tier: Warm-up
Lesson: 00.2

For each snippet, write its TIME complexity as a string, like "O(n)", "O(n log n)",
"O(n^2)", "O(log n)", "O(1)". Spaces and capitals don't matter.
The last two (s1, s2) ask for SPACE complexity: extra memory, not counting the input.

n = len(nums). Assume nums is a list unless it says otherwise.
Answers with reasons: solutions/lab_01_bigo_spotter_answers.md
"""

# b1
# for i in range(n):
#     for j in range(10):
#         total += i * j

# b2
# i = 1
# while i < n:
#     i *= 2

# b3
# nums.sort()
# for x in nums:
#     print(x)

# b4
# for x in nums:
#     if x + 1 in nums:        # nums is a LIST
#         count += 1

# b5
# seen = set(nums)
# for x in nums:
#     if x + 1 in seen:        # seen is a SET
#         count += 1

# b6
# for i in range(n):
#     for j in range(i + 1, n):
#         if nums[i] == nums[j]:
#             return True

# b7
# ages = {"ana": 31, "bo": 25, ...}    # n entries
# print(ages["bo"])

# b8
# for x in nums:
#     total += x
# for x in nums:
#     biggest = max(biggest, x)

# b9
# while nums:
#     first = nums.pop(0)
#     print(first)

# b10
# parts = []
# for word in words:            # n words, each short
#     parts.append(word.upper())
# result = " ".join(parts)

# b11
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             grid_total += i + j + k

# b12
# lo, hi = 0, n - 1
# while lo <= hi:
#     mid = (lo + hi) // 2
#     if nums[mid] == target:
#         return mid
#     elif nums[mid] < target:
#         lo = mid + 1
#     else:
#         hi = mid - 1

# s1  (SPACE)
# seen = set()
# for x in nums:
#     seen.add(x)

# s2  (SPACE)
# left, right = 0, n - 1
# while left < right:
#     nums[left], nums[right] = nums[right], nums[left]
#     left += 1
#     right -= 1


ANSWERS = {
    "b1": ...,
    "b2": ...,
    "b3": ...,
    "b4": ...,
    "b5": ...,
    "b6": ...,
    "b7": ...,
    "b8": ...,
    "b9": ...,
    "b10": ...,
    "b11": ...,
    "b12": ...,
    "s1": ...,
    "s2": ...,
}

# ---------- tests: don't edit below ----------
from _check import check_answers

KEY = {'b1': '834f60532f9e68b2', 'b2': 'c70b0971e96739e6', 'b3': '8179fa64a30652c7', 'b4': '1ae01689aa5f5982', 'b5': 'a6530e64887fc39e', 'b6': 'ac4df317f2874fd9', 'b7': '04bf7ce41ac4f2a7', 'b8': 'f16e63be820c075e', 'b9': '4628d4138eb1868a', 'b10': '176a66a0abb87a06', 'b11': 'ac013370fdc9c7ad', 'b12': '8004a9be90fd4eec', 's1': 'a951ae26420dbddd', 's2': '16145d8036d1953f'}
STUDY = {
    'b1': 'lessons/00.2-big-o.md › Drop constants (inner loop of 10 is a constant)',
    'b2': 'lessons/00.2-big-o.md › The halving loop: O(log n)',
    'b3': 'lessons/00.2-big-o.md › Worked trace C: sort + loop, the bigger term wins',
    'b4': 'lessons/00.2-big-o.md › Hidden loops: `in` on a list',
    'b5': 'lessons/00.2-big-o.md › Hidden loops: `in` on a set is O(1)',
    'b6': 'lessons/00.2-big-o.md › Loops inside loops multiply',
    'b7': 'lessons/00.2-big-o.md › The ladder: dict lookup is O(1)',
    'b8': 'lessons/00.2-big-o.md › Loops in a row add',
    'b9': 'lessons/00.2-big-o.md › Hidden loops: pop(0)',
    'b10': 'lessons/00.2-big-o.md › Hidden loops: append and join',
    'b11': 'lessons/00.2-big-o.md › Loops inside loops multiply (three deep)',
    'b12': 'lessons/00.2-big-o.md › The halving loop (binary search)',
    's1': 'lessons/00.2-big-o.md › Space complexity',
    's2': 'lessons/00.2-big-o.md › Space complexity: in-place swaps use O(1)',
}
ENTRY = "ANSWERS"


def run_tests(answers):
    return check_answers(answers, KEY, title="Big-O answers", study=STUDY)


if __name__ == "__main__":
    run_tests(ANSWERS)
