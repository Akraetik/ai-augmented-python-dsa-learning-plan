"""
SOLUTION — Lab 2.06 3Sum (LeetCode 15)
Time O(n²). Space O(1) beyond the sort and output.

Sort. For each i, two-pointer the rest for a pair summing to -nums[i].
Skip duplicates in three places:
  1. fixed value: skip if nums[i] == nums[i - 1]  (keeps the FIRST copy, so [-1, -1, 2] is found)
  2. after a match: move left past equal values
  3. after a match: move right past equal values
Early exit: if nums[i] > 0, nothing to the right can bring the sum back to 0.
"""
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    n = len(nums)
    out = []
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                out.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return out
