# Section 03 · Hint Ladder

One hint at a time. Ten more minutes of effort after each.
Needed Hint 3? Mark the lab **assisted** in PROGRESS.md. It comes back as a cold solve.

---

### 3.01 Maximum Average Subarray I
<details><summary>Hint 1</summary>When the window slides one step, how many items change? Which ones?</details>
<details><summary>Hint 2</summary>Build the first window's sum once. Each step: add <code>nums[right]</code>, subtract <code>nums[right - k]</code>. Track the best sum; divide by k at the end.</details>
<details><summary>Hint 3</summary>

```
window = sum(nums[:k]); best = window
for right in range(k, len(nums)):
    window += nums[right] - nums[right - k]
    best = max(best, window)
return best / k
```
</details>

### 3.02 Permutation in String
<details><summary>Hint 1</summary>"abc" and "cab" are rearrangements of each other. What's the same about them?</details>
<details><summary>Hint 2</summary>Same letter counts. Slide a window of len(s1) over s2, keeping a 26-slot count list. Compare with s1's counts each step.</details>
<details><summary>Hint 3</summary>For each i: window[s2[i]] += 1; if i ≥ m: window[s2[i − m]] −= 1; if window == need: return True. After the loop: return False.</details>

### 3.03 Longest Substring Without Repeating Characters
<details><summary>Hint 1</summary>When a letter repeats, which part of the window has to go?</details>
<details><summary>Hint 2</summary>Keep a set of the window's letters. Before adding s[right], remove s[left] and move left WHILE s[right] is still in the set.</details>
<details><summary>Hint 3</summary>

```
for right, ch in enumerate(s):
    while ch in seen: seen.remove(s[left]); left += 1
    seen.add(ch)
    best = max(best, right - left + 1)
```
</details>

### 3.04 Max Consecutive Ones III
<details><summary>Hint 1</summary>You never flip anything. Describe a good window using only the word "zeros."</details>
<details><summary>Hint 2</summary>The longest window with at most k zeros. Count zeros in the window; shrink while the count is above k.</details>
<details><summary>Hint 3</summary>On a 0, zeros += 1. While zeros &gt; k: if nums[left] == 0: zeros −= 1; left += 1. Then record right − left + 1.</details>

### 3.05 Longest Repeating Character Replacement
<details><summary>Hint 1</summary>In "AABAB", which letter would you keep, and how many letters would you change?</details>
<details><summary>Hint 2</summary>Changes needed = window length − count of the most common letter in it. Shrink while that's more than k.</details>
<details><summary>Hint 3</summary>Keep a 26-slot count list. After adding s[right]: while (right − left + 1) − max(counts) &gt; k: counts[s[left]] −= 1; left += 1. Record the length.</details>

### 3.06 Minimum Size Subarray Sum
<details><summary>Hint 1</summary>Once a window's sum is big enough, could a shorter window ending at the same spot also work?</details>
<details><summary>Hint 2</summary>Shortest-valid template: grow; WHILE the sum ≥ target, record the length, then drop nums[left]. Start best at infinity.</details>
<details><summary>Hint 3</summary>

```
for right, x in enumerate(nums):
    total += x
    while total >= target:
        best = min(best, right - left + 1)
        total -= nums[left]; left += 1
return 0 if best == inf else best
```
</details>

### 3.07 Minimum Window Substring
<details><summary>Hint 1</summary>How can you tell, cheaply, that a window has every letter t needs, with enough copies?</details>
<details><summary>Hint 2</summary>need = Counter(t), required = len(need). have counts letters whose window count has reached need. Valid when have == required.</details>
<details><summary>Hint 3</summary>On enter: if window[ch] == need[ch]: have += 1. While have == required: record (start, length); on leaving char out: if window[out] &lt; need[out]: have −= 1; left += 1. Return the best slice.</details>

### 3.08 Substring with Concatenation of All Words
<details><summary>Hint 1</summary>All words are length L. If you chop s into L-letter pieces starting at 0, which match starts can you find? Which can't you?</details>
<details><summary>Hint 2</summary>Run one window for each offset 0..L−1, stepping L at a time. Inside, it's a variable window of pieces with counts.</details>
<details><summary>Hint 3</summary>Piece not a word → clear and restart after it. Add piece; while its count &gt; need: drop the leftmost piece. If the window holds len(words) pieces: record left, drop the leftmost piece.</details>

### 3.09 Bug Hunt
<details><summary>Hint 1</summary>Trace "pwwkew". What happens when the second w arrives? Is the window valid after one step left?</details>
<details><summary>Hint 2</summary>The known bugs are M4, M5, M7. The new one is about <code>if</code> vs <code>while</code>.</details>
<details><summary>Hint 3</summary><code>if</code> → <code>while</code>. <code>left + 1</code> → <code>left += 1</code>. <code>right − left</code> → <code>right − left + 1</code>. Move <code>return best</code> out of the loop.</details>
