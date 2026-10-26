"""
SOLUTION — Lab 1.25 Bug Hunt: Move Zeroes

The four bugs:
1. range(1, len(nums)) skips index 0.            -> M5. Fix: range(len(nums))
2. nums[write] = read copies the INDEX.          -> M1. Fix: nums[write] = nums[read]
3. write + 1 is never saved.                     -> M4. Fix: write += 1
4. return nums[:write] — the signature is None.  -> M6. Fix: delete the return

Time O(n). Space O(1).
"""
from typing import List


def move_zeroes(nums: List[int]) -> None:
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1
    for i in range(write, len(nums)):
        nums[i] = 0
