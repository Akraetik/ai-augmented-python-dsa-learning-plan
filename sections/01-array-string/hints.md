# Section 01 · Hint Ladder

One hint at a time. Ten more minutes of effort after each.
Needed Hint 3? Mark the lab **assisted** in PROGRESS.md. It comes back as a cold solve.

---

### 1.01 Merge Sorted Array
<details><summary>Hint 1</summary>Where in nums1 is there free space? What's the biggest number overall, and where does it belong?</details>
<details><summary>Hint 2</summary>Fill from the back with three pointers: last real item of nums1, last item of nums2, last slot. Place the bigger one.</details>
<details><summary>Hint 3</summary>

```
p1, p2, w = m-1, n-1, m+n-1
while p2 >= 0:
    if p1 >= 0 and nums1[p1] > nums2[p2]: nums1[w] = nums1[p1]; p1 -= 1
    else: nums1[w] = nums2[p2]; p2 -= 1
    w -= 1
```
</details>

### 1.02 Remove Element
<details><summary>Hint 1</summary>As you read each item, how do you decide if it stays? Where does a "stay" item go?</details>
<details><summary>Hint 2</summary>Read/write pointers. Keep rule: <code>nums[read] != val</code>.</details>
<details><summary>Hint 3</summary>

```
write = 0
for read in range(len(nums)):
    if nums[read] != val: nums[write] = nums[read]; write += 1
return write
```
</details>

### 1.03 Remove Duplicates
<details><summary>Hint 1</summary>The list is sorted. Where do duplicates of a value sit?</details>
<details><summary>Hint 2</summary>Keep the item if it differs from the last KEPT item, <code>nums[write - 1]</code>. Always keep the first.</details>
<details><summary>Hint 3</summary>

```
write = 0
for read in range(len(nums)):
    if write == 0 or nums[read] != nums[write-1]: copy and write += 1
return write
```
</details>

### 1.04 Remove Duplicates II
<details><summary>Hint 1</summary>If the item two kept slots back equals this one, how many copies would this make?</details>
<details><summary>Hint 2</summary>Keep if <code>write &lt; 2</code> or <code>nums[read] != nums[write - 2]</code>.</details>
<details><summary>Hint 3</summary>Same skeleton as 1.03. Only the keep rule changes to the line in Hint 2.</details>

### 1.05 Majority Element
<details><summary>Hint 1</summary>Which tool counts things in one line? After sorting, where must the majority sit?</details>
<details><summary>Hint 2</summary>For O(1) space: Boyer–Moore. One candidate, one count. Equal → +1, different → −1, zero → new candidate.</details>
<details><summary>Hint 3</summary>

```
cand, count = None, 0
for x in nums:
    if count == 0: cand = x
    count += 1 if x == cand else -1
return cand
```
</details>

### 1.06 H-Index
<details><summary>Hint 1</summary>Sort biggest first. For paper number i (starting at 1), what must be true for h to be at least i?</details>
<details><summary>Hint 2</summary>Walk the sorted list. While <code>citations ≥ paper number</code>, h = paper number. Stop at the first failure.</details>
<details><summary>Hint 3</summary>

```
for i, c in enumerate(sorted(citations, reverse=True), start=1):
    if c >= i: h = i
    else: break
```
</details>

### 1.07 Rotate Array
<details><summary>Hint 1</summary>What should you do to k when it's bigger than the list? Where does index i end up?</details>
<details><summary>Hint 2</summary><code>k %= n</code>. With an extra list: <code>new[(i + k) % n] = nums[i]</code>, then <code>nums[:] = new</code>. O(1): three reversals.</details>
<details><summary>Hint 3</summary>reverse(0, n−1), then reverse(0, k−1), then reverse(k, n−1). Write a helper that reverses between two indexes.</details>

### 1.08 Best Time to Buy and Sell Stock
<details><summary>Hint 1</summary>If you sell today, what's the best day you could have bought? Do you need to search for it, or can you remember it?</details>
<details><summary>Hint 2</summary>Track the lowest price so far and the best profit so far.</details>
<details><summary>Hint 3</summary>

```
lowest, best = inf, 0
for p in prices: lowest = min(lowest, p); best = max(best, p - lowest)
```
</details>

### 1.09 Best Time to Buy and Sell Stock II
<details><summary>Hint 1</summary>Draw it. Is a long climb worth more than the sum of its daily steps?</details>
<details><summary>Hint 2</summary>No — they're equal. So collect every positive day-to-day difference.</details>
<details><summary>Hint 3</summary>For i from 1: if prices[i] &gt; prices[i−1], add the difference.</details>

### 1.10 Jump Game
<details><summary>Hint 1</summary>Instead of trying paths, what single number could summarize "how far can I get so far"?</details>
<details><summary>Hint 2</summary>Track <code>reach</code>. If <code>i &gt; reach</code>, you're stuck. Else <code>reach = max(reach, i + nums[i])</code>.</details>
<details><summary>Hint 3</summary>

```
reach = 0
for i, step in enumerate(nums):
    if i > reach: return False
    reach = max(reach, i + step)
return True
```
</details>

### 1.11 Jump Game II
<details><summary>Hint 1</summary>Which indexes can you reach with exactly 1 jump? With 2? Think in rings.</details>
<details><summary>Hint 2</summary>Variables: jumps, ring_end, farthest. Loop i up to len−2. Update farthest. When i == ring_end: jumps += 1, ring_end = farthest.</details>
<details><summary>Hint 3</summary>

```
jumps = ring_end = farthest = 0
for i in range(len(nums) - 1):
    farthest = max(farthest, i + nums[i])
    if i == ring_end: jumps += 1; ring_end = farthest
return jumps
```
</details>

### 1.12 Gas Station
<details><summary>Hint 1</summary>If total gas is less than total cost, what's the answer? If you run dry at station j after starting at s, could any station between them work?</details>
<details><summary>Hint 2</summary>No. So when the running tank goes negative at i, set start = i + 1 and reset the tank.</details>
<details><summary>Hint 3</summary>

```
if sum(gas) < sum(cost): return -1
start = tank = 0
for i: tank += gas[i] - cost[i]; if tank < 0: start = i + 1; tank = 0
return start
```
</details>

### 1.13 Product of Array Except Self
<details><summary>Hint 1</summary>Split "everything except i" into two groups. What are they?</details>
<details><summary>Hint 2</summary>Everything left of i, times everything right of i. Build left products in one pass, right products in another.</details>
<details><summary>Hint 3</summary>Pass 1: out[i] = running left product, then multiply nums[i] in. Pass 2 (backward): out[i] *= running right product, then multiply nums[i] in.</details>

### 1.14 Trapping Rain Water
<details><summary>Hint 1</summary>Look at one index. What two bars decide how high water can rise above it?</details>
<details><summary>Hint 2</summary>The tallest bar to the left and the tallest to the right. Water = min(the two) − own height.</details>
<details><summary>Hint 3</summary>Precompute max_left[i] (running max left→right) and max_right[i] (running max right→left). Sum min(max_left[i], max_right[i]) − height[i].</details>

### 1.15 Candy
<details><summary>Hint 1</summary>There are two rules: one about your left neighbor, one about your right. Can you satisfy them one at a time?</details>
<details><summary>Hint 2</summary>Left→right sweep handles the left rule. Right→left sweep handles the right rule, using max() so you don't break the first.</details>
<details><summary>Hint 3</summary>

```
give = [1]*n
for i in 1..n-1: if r[i] > r[i-1]: give[i] = give[i-1] + 1
for i in n-2..0: if r[i] > r[i+1]: give[i] = max(give[i], give[i+1] + 1)
return sum(give)
```
</details>

### 1.16 Insert Delete GetRandom O(1)
<details><summary>Hint 1</summary>Which structure gives O(1) random picks? Which gives O(1) "is it here, and where"?</details>
<details><summary>Hint 2</summary>A list for values and a dict value → index. Remove by swapping with the last element, then pop.</details>
<details><summary>Hint 3</summary>remove(val): i = index_of[val]; last = values[−1]; values[i] = last; index_of[last] = i; values.pop(); del index_of[val].</details>

### 1.17 Length of Last Word
<details><summary>Hint 1</summary>Which string method throws away all the spaces for you?</details>
<details><summary>Hint 2</summary><code>len(s.split()[-1])</code>. Without split: skip trailing spaces from the end, then count non-spaces.</details>
<details><summary>Hint 3</summary>Two while loops from i = len(s) − 1, each guarded with <code>i &gt;= 0 and ...</code>.</details>

### 1.18 Longest Common Prefix
<details><summary>Hint 1</summary>Say it: "One pass of my outer loop = one character position." What does the inner loop walk over?</details>
<details><summary>Hint 2</summary>For each column of the first word, check every other word: too short, or different letter → stop.</details>
<details><summary>Hint 3</summary>

```
for col, ch in enumerate(strs[0]):
    for w in strs[1:]:
        if col >= len(w) or w[col] != ch: return strs[0][:col]
return strs[0]
```
</details>

### 1.19 Reverse Words in a String
<details><summary>Hint 1</summary>What does <code>split()</code> with no argument do to extra spaces?</details>
<details><summary>Hint 2</summary>Split, reverse the list, join with one space.</details>
<details><summary>Hint 3</summary><code>" ".join(reversed(s.split()))</code>. For the manual version: skip spaces, mark a start, walk to the next space, slice the word.</details>

### 1.20 Find First Occurrence
<details><summary>Hint 1</summary>At which positions could the needle possibly start? What's the last one?</details>
<details><summary>Hint 2</summary>Starts run from 0 to len(haystack) − len(needle), inclusive. At each, compare characters until one differs.</details>
<details><summary>Hint 3</summary>

```
for start in range(n - m + 1):
    j = 0
    while j < m and hay[start+j] == needle[j]: j += 1
    if j == m: return start
return -1
```
</details>

### 1.21 Roman to Integer
<details><summary>Hint 1</summary>In "IV", what tells you to subtract the I instead of adding it?</details>
<details><summary>Hint 2</summary>If the next symbol is bigger, subtract this one. Else add it. Use a dict of values.</details>
<details><summary>Hint 3</summary>Loop i over s. <code>if i + 1 &lt; len(s) and V[s[i+1]] &gt; V[s[i]]: total -= V[s[i]] else: total += V[s[i]]</code></details>

### 1.22 Integer to Roman
<details><summary>Hint 1</summary>To write 1994, what's the biggest Roman piece that fits first?</details>
<details><summary>Hint 2</summary>Greedy with 13 pieces, biggest first, including CM, CD, XC, XL, IX, IV.</details>
<details><summary>Hint 3</summary>For each (value, symbol): while num ≥ value, append symbol and subtract. Or use divmod.</details>

### 1.23 Zigzag Conversion
<details><summary>Hint 1</summary>Forget formulas. If you had one bucket per row, which bucket gets each letter?</details>
<details><summary>Hint 2</summary>Current row plus a step of +1 or −1. Flip at row 0 and the last row. Special-case num_rows == 1.</details>
<details><summary>Hint 3</summary>rows = [[] for each row]; for ch: rows[row].append(ch); flip step at the ends; row += step. Join all rows.</details>

### 1.24 Text Justification
<details><summary>Hint 1</summary>Split the job: (a) which words fit on this line, (b) how to space a full line, (c) how to space the last line.</details>
<details><summary>Hint 2</summary>A line fits while letters + (word count − 1) ≤ width. Spaces to spread = width − letters. <code>divmod(spaces, gaps)</code>.</details>
<details><summary>Hint 3</summary>Each of the first <code>extra</code> gaps gets <code>base + 1</code> spaces, the rest get <code>base</code>. Last line and single-word lines: <code>" ".join(...)</code> then pad right.</details>

### 1.25 Bug Hunt: Move Zeroes
<details><summary>Hint 1</summary>Trace [0, 1, 0, 3, 12]. What does the loop do at index 0? What value gets written?</details>
<details><summary>Hint 2</summary>The four bugs match M1, M4, M5, and M6.</details>
<details><summary>Hint 3</summary>The range skips 0. It writes <code>read</code> (an index). <code>write + 1</code> isn't saved. It returns something when the signature says None.</details>
