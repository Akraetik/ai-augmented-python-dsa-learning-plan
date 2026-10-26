"""
SOLUTION — Lab 1.13 Product of Array Except Self (LeetCode 238)
Time O(n). Space O(1) extra (the output list doesn't count).

answer[i] = (product of everything left of i) * (product of everything right of i).
Pass 1 writes left products straight into `out`. Pass 2 walks right to left with one running
`right` product and multiplies it in. Record first, then include yourself — so i is never in its own product.
No division, so zeros need no special case.
"""
from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    out = [1] * n
    left = 1
    for i in range(n):
        out[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):
        out[i] *= right
        right *= nums[i]
    return out
