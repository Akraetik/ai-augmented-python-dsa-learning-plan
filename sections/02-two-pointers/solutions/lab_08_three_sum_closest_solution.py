"""
SOLUTION — Lab 2.08 3Sum Closest (LeetCode 16)
Time O(n²). Space O(1) beyond the sort.
Same loop as 3Sum. Track the sum with the smallest distance to target. Exact hit → return at once.
No duplicate skipping needed: only one number is returned.
"""
from typing import List


def three_sum_closest(nums: List[int], target: int) -> int:
    nums = sorted(nums)
    n = len(nums)
    best = nums[0] + nums[1] + nums[2]
    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if abs(total - target) < abs(best - target):
                best = total
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return total
    return best
