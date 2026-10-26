"""
SOLUTION — Lab 1.11 Jump Game II (LeetCode 45)
Time O(n). Space O(1).
Walk the current "ring" of indexes reachable with `jumps` jumps. Track the farthest the next ring
reaches. When you reach the end of the current ring, you must jump: count it, and the next ring's
farthest becomes the new ring end. Loop to len - 1: standing on the last index needs no more jumps.
"""
from typing import List


def jump(nums: List[int]) -> int:
    jumps = 0
    ring_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == ring_end:
            jumps += 1
            ring_end = farthest
    return jumps
