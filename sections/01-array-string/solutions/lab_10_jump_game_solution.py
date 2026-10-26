"""
SOLUTION — Lab 1.10 Jump Game (LeetCode 55)
Time O(n). Space O(1).
reach = farthest index reachable so far. If i > reach, index i can't be reached: stuck.
Otherwise extend reach with i + nums[i]. Early exit once reach covers the last index.

Alternative: walk backward, keeping the leftmost index that can reach the end ("goal").
"""
from typing import List


def can_jump(nums: List[int]) -> bool:
    reach = 0
    last = len(nums) - 1
    for i, step in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + step)
        if reach >= last:
            return True
    return True
