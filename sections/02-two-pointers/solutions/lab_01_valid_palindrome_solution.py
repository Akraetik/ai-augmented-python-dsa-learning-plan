"""
SOLUTION — Lab 2.01 Valid Palindrome (LeetCode 125)

Way 1 (O(n) space):
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]

Way 2 (below, O(1) space): two pointers, skip junk in place.
Each skip loop also checks left < right, so an all-junk string can't run off the end.
"""


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
