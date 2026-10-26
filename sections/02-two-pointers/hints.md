# Section 02 · Hint Ladder

One hint at a time. Ten more minutes of effort after each.
Needed Hint 3? Mark the lab **assisted** in PROGRESS.md. It comes back as a cold solve.

---

### 2.01 Valid Palindrome
<details><summary>Hint 1</summary>Which two characters must match first? What do you do with a comma?</details>
<details><summary>Hint 2</summary>Two pointers from the ends. Skip non-alphanumeric characters with inner while loops that also check <code>left &lt; right</code>. Compare lowercased.</details>
<details><summary>Hint 3</summary>

```
while left < right:
    while left < right and not s[left].isalnum(): left += 1
    while left < right and not s[right].isalnum(): right -= 1
    if s[left].lower() != s[right].lower(): return False
    left += 1; right -= 1
return True
```
</details>

### 2.02 Is Subsequence
<details><summary>Hint 1</summary>Walk t one character at a time. When does your place in s change?</details>
<details><summary>Hint 2</summary>i in s moves only when <code>t[j] == s[i]</code>. j moves every step. Done when i reaches len(s).</details>
<details><summary>Hint 3</summary>

```
i = 0
for ch in t:
    if i < len(s) and ch == s[i]: i += 1
return i == len(s)
```
</details>

### 2.03 Two Sum II
<details><summary>Hint 1</summary>Start with the smallest and the biggest. If their sum is too small, which number could possibly help?</details>
<details><summary>Hint 2</summary>Too small → left += 1. Too big → right −= 1. Return positions + 1.</details>
<details><summary>Hint 3</summary>Loop while left &lt; right: compute total; equal → <code>[left + 1, right + 1]</code>; less → left += 1; more → right −= 1.</details>

### 2.04 Squares of a Sorted Array
<details><summary>Hint 1</summary>In <code>[-4, -1, 0, 3, 10]</code>, where are the two biggest squares?</details>
<details><summary>Hint 2</summary>At the ends. Fill the output from its LAST slot, taking whichever end has the bigger absolute value.</details>
<details><summary>Hint 3</summary>For write from n−1 down to 0: if abs(nums[left]) &gt; abs(nums[right]) put nums[left]² and left += 1, else put nums[right]² and right −= 1.</details>

### 2.05 Container With Most Water
<details><summary>Hint 1</summary>Start with the widest container. To possibly do better while getting narrower, what must happen to the height?</details>
<details><summary>Hint 2</summary>Move the shorter line inward. Keeping it can never beat the current area.</details>
<details><summary>Hint 3</summary>

```
while left < right:
    best = max(best, (right - left) * min(h[left], h[right]))
    if h[left] < h[right]: left += 1
    else: right -= 1
```
</details>

### 2.06 3Sum
<details><summary>Hint 1</summary>If you fix the first number, what problem is left? You solved it in lab 03.</details>
<details><summary>Hint 2</summary>Sort. For each i, Two Sum II on i+1..n−1 for target −nums[i]. Skip repeated fixed values and, after a match, skip repeated left/right values.</details>
<details><summary>Hint 3</summary>

```
nums.sort()
for i: if i > 0 and nums[i] == nums[i-1]: continue
    left, right = i + 1, n - 1
    while left < right:
        total < 0 → left += 1;  total > 0 → right -= 1
        else: record; left += 1; right -= 1
              while left < right and nums[left] == nums[left-1]: left += 1
              while left < right and nums[right] == nums[right+1]: right -= 1
```
</details>

### 2.07 Trapping Rain Water, Two Pointers
<details><summary>Hint 1</summary>To know the water at one bar, do you need both maxes exactly, or only the smaller one?</details>
<details><summary>Hint 2</summary>Keep left_max and right_max. The side with the smaller max has a known water level. Add its water and move it.</details>
<details><summary>Hint 3</summary>Each step: update both maxes. If left_max &lt; right_max: total += left_max − h[left]; left += 1. Else the mirror on the right.</details>

### 2.08 3Sum Closest
<details><summary>Hint 1</summary>What changes from 3Sum if you only need the best sum, not every triple?</details>
<details><summary>Hint 2</summary>Same sorted loop. Update best when <code>abs(total − target)</code> shrinks. Move left if total &lt; target, right if bigger, return if equal.</details>
<details><summary>Hint 3</summary>Start best as the sum of the first three sorted numbers. No duplicate skipping needed.</details>

### 2.09 Bug Hunt: Two Sum II
<details><summary>Hint 1</summary>Trace it. What index does <code>right</code> start at? What happens on the first line inside the loop?</details>
<details><summary>Hint 2</summary>The known ones are M4, M5, M6. The new one is about which pointer moves when the sum is too small.</details>
<details><summary>Hint 3</summary>Start <code>right</code> at len − 1. Return 1-indexed. Too small should move <code>left</code>, too big should move <code>right</code>. And <code>left + 1</code> must be <code>left += 1</code>.</details>
