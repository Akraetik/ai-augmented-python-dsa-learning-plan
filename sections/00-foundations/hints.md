# Section 00 · Hint Ladder

Open one hint at a time. Try for 10 more minutes after each one.
If you needed Hint 3, mark the lab "assisted" in PROGRESS.md.

---

### Lab 0.02 — Total, Biggest, Smallest
<details><summary>Hint 1</summary>Before the loop, what values should total, biggest, and smallest hold? What if every number is negative?</details>
<details><summary>Hint 2</summary>Running values: start biggest and smallest at <code>nums[0]</code>. Each item either beats them or doesn't.</details>
<details><summary>Hint 3</summary>

```
total = 0; biggest = smallest = first item
for each x:
    total += x
    if x > biggest: biggest = x
    if x < smallest: smallest = x
return the three
```
</details>

### Lab 0.03 — Count the Letters
<details><summary>Hint 1</summary>Which string method tells you if a character is a letter? Which one makes it lowercase?</details>
<details><summary>Hint 2</summary>Counting pattern: <code>counts[key] = counts.get(key, 0) + 1</code>. The <code>=</code> matters (M4).</details>
<details><summary>Hint 3</summary>

```
counts = {}
for ch in s:
    if ch is a letter:
        key = ch lowercased
        counts[key] = counts.get(key, 0) + 1
return counts
```
</details>

### Lab 0.04 — Reverse a List In Place
<details><summary>Hint 1</summary>Which two items trade places first? Which two next? Draw it for 4 items and 5 items.</details>
<details><summary>Hint 2</summary>Two pointers: one at index 0, one at the last index. Swap, step inward. Stop when they meet.</details>
<details><summary>Hint 3</summary>

```
left, right = 0, len - 1
while left < right:
    swap nums[left] and nums[right]
    left += 1; right -= 1
```
</details>

### Lab 0.05 — Contains Duplicate
<details><summary>Hint 1</summary>As you walk the list, what do you need to remember about the numbers behind you?</details>
<details><summary>Hint 2</summary>"Have I seen this before?" → a set. Checking a set is O(1).</details>
<details><summary>Hint 3</summary>

```
seen = empty set
for x in nums:
    if x in seen: return True
    add x to seen
return False
```
</details>

### Lab 0.06 — Running Sum
<details><summary>Hint 1</summary>If you know answer[3], how do you get answer[4] with one addition?</details>
<details><summary>Hint 2</summary>Keep one running total variable. Each step: add the current number, append the total.</details>
<details><summary>Hint 3</summary>

```
total = 0; out = []
for x in nums:
    total += x
    out.append(total)
return out
```
</details>

### Lab 0.07 — Max Consecutive Ones
<details><summary>Hint 1</summary>What two numbers do you need to know at every step?</details>
<details><summary>Hint 2</summary>"current run" resets on a 0. "best" is updated whenever current grows, not only when the run ends.</details>
<details><summary>Hint 3</summary>

```
best = current = 0
for x in nums:
    if x == 1: current += 1; best = max(best, current)
    else: current = 0
return best
```
</details>

### Lab 0.08 — Valid Anagram
<details><summary>Hint 1</summary>If the lengths differ, can they be anagrams? What else must match?</details>
<details><summary>Hint 2</summary>Way 1: sorted letters must be identical. Way 2: letter counts must be identical.</details>
<details><summary>Hint 3</summary>

```
if lengths differ: return False
return Counter(s) == Counter(t)        # or sorted(s) == sorted(t)
```
</details>

### Lab 0.09 — Two Sum
<details><summary>Hint 1</summary>Standing on the number 2 with target 7, what number are you hoping to have seen already?</details>
<details><summary>Hint 2</summary>Store each value you pass in a dict: value → index. Look up <code>target - x</code> before you store x.</details>
<details><summary>Hint 3</summary>

```
index_of = {}
for i, x in enumerate(nums):
    if target - x in index_of: return [index_of[target - x], i]
    index_of[x] = i
```
</details>

### Lab 0.10 — Speed Trap
<details><summary>Hint 1</summary>Look at the Lesson 00.2 table. What does <code>x in a</code> cost when <code>a</code> is a list?</details>
<details><summary>Hint 2</summary>Convert once, outside the loop, to a structure with O(1) membership.</details>
<details><summary>Hint 3</summary>Add <code>in_a = set(a)</code> before the loop. Check <code>x in in_a</code>.</details>

### Lab 0.11 — Bug Hunt
<details><summary>Hint 1</summary>Trace "aabbc" on paper. What's in <code>counts</code> after the first loop?</details>
<details><summary>Hint 2</summary>The bugs are M4, M5, M6, and M7. One each.</details>
<details><summary>Hint 3</summary>Line 1 never saves the count. The range skips index 0. It returns a character, not an index. The <code>else: return -1</code> quits too early.</details>
