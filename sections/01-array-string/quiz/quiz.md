# Section 01 · Array / String Checkpoint

32 questions · pass mark 85% · no notes, no IDE, no AI. Answers: [quiz_answers.md](quiz_answers.md). Better: open `quiz.html` in a browser for instant scoring by topic.

**1.** *(Read/write pointers (1.1))* In the read/write pointer pattern, when does `write` move?

- A. Every step
- B. Only when an item is kept
- C. Only when an item is skipped
- D. When read reaches the end

**2.** *(Read/write pointers (1.1))* Remove Duplicates (sorted). What does this return for `[1, 1, 1, 2]`?

```python
write = 0
for read in range(len(nums)):
    if write == 0 or nums[read] != nums[write - 1]:
        nums[write] = nums[read]
        write += 1
return write
```

- A. 1
- B. 2
- C. 3
- D. 4

**3.** *(Read/write pointers (1.1))* Remove Duplicates II allows each value twice. Which keep rule is right?

- A. `nums[read] != nums[read - 1]`
- B. `write < 2 or nums[read] != nums[write - 2]`
- C. `nums[read] != nums[write - 1]`
- D. `nums[read] != nums[read - 2]`

**4.** *(Read/write pointers (1.1))* Why does Merge Sorted Array fill nums1 from the back?

- A. It's faster to index from the end
- B. The back is empty space, so nothing unread gets overwritten
- C. Python lists only append at the end
- D. The problem requires descending order

**5.** *(Read/write pointers (1.1))* A function ends with `nums = new_list`. The signature is `-> None`. What does the caller see?

- A. The new list
- B. The original list, unchanged
- C. None
- D. An error

**6.** *(Counting and voting (1.2))* Boyer–Moore voting on `[5, 1, 5, 2, 5]`. Final candidate?

- A. 1
- B. 2
- C. 5
- D. None

**7.** *(Counting and voting (1.2))* Why is Boyer–Moore only safe for Majority Element because a majority is guaranteed?

- A. It needs sorted input
- B. Without a majority, the leftover candidate may not be one; you'd need a second counting pass
- C. It only works on positive numbers
- D. It's O(n²) otherwise

**8.** *(Counting and voting (1.2))* H-Index of `[10, 8, 5, 4, 3]`?

- A. 3
- B. 4
- C. 5
- D. 8

**9.** *(Index math and rotation (1.3))* Rotate right by k = 10 on a list of length 7. What k do you actually rotate by?

- A. 10
- B. 7
- C. 3
- D. 4

**10.** *(Index math and rotation (1.3))* Three-reversal rotation (right by k). The correct order is:

- A. reverse first k, reverse rest, reverse all
- B. reverse all, reverse first k, reverse rest
- C. reverse last k, reverse all
- D. reverse all twice

**11.** *(Index math and rotation (1.3))* Popping from the end and inserting at index 0, k times, on 100,000 items. Why too slow?

- A. pop() is O(n)
- B. insert(0, x) is O(n), done k times → O(n·k)
- C. It uses too much memory
- D. It's not slow

**12.** *(Best-so-far scans (1.4))* Best Time to Buy and Sell (one trade) on `[4, 9, 1, 6]`. Answer?

- A. 5
- B. 8
- C. 6
- D. 3

**13.** *(Best-so-far scans (1.4))* What do you track in a single pass for one-trade stock profit?

- A. Highest price so far
- B. Lowest price so far and best profit so far
- C. Every pair's difference
- D. The average price

**14.** *(Best-so-far scans (1.4))* Stock II (unlimited trades) on `[1, 3, 2, 5]`. Answer?

- A. 4
- B. 5
- C. 3
- D. 6

**15.** *(Reach and greedy (1.5))* Jump Game on `[2, 0, 0, 1]`. Reachable?

- A. True
- B. False

**16.** *(Reach and greedy (1.5))* Jump Game II. When do you add one to the jump count?

- A. Every index
- B. When i reaches the end of the current ring
- C. When nums[i] is the biggest so far
- D. When farthest changes

**17.** *(Reach and greedy (1.5))* Gas Station: running tank goes negative at station 6, start was 2. Next start candidate?

- A. 3
- B. 6
- C. 7
- D. 0

**18.** *(Reach and greedy (1.5))* Gas Station: total gas is 20, total cost is 21. Answer?

- A. 0
- B. -1
- C. The station with the most gas
- D. Depends on order

**19.** *(Prefix and suffix passes (1.6))* Product Except Self on `[2, 3, 4]`. Left-products row (strictly left of i)?

- A. [2, 6, 24]
- B. [1, 2, 6]
- C. [0, 2, 6]
- D. [1, 3, 12]

**20.** *(Prefix and suffix passes (1.6))* Why does Product Except Self forbid division?

- A. Division is slow
- B. A zero in the list breaks total ÷ nums[i]
- C. Python can't divide lists
- D. Floats lose precision only

**21.** *(Prefix and suffix passes (1.6))* Trapping Rain Water: water above index i equals

- A. max(max_left, max_right) − height[i]
- B. min(max_left, max_right) − height[i]
- C. height[i] − min(neighbors)
- D. max_left − max_right

**22.** *(Prefix and suffix passes (1.6))* Candy: why `max()` in the right-to-left sweep?

- A. To keep the left-neighbor rule from sweep one
- B. To make the total smaller
- C. Because ratings can be negative
- D. It isn't needed

**23.** *(List + dict design (1.7))* RandomizedSet remove(val) in O(1). Which step is essential?

- A. `values.remove(val)`
- B. Swap val's slot with the last value, update that value's index, pop the end
- C. Sort the list first
- D. Rebuild the dict

**24.** *(List + dict design (1.7))* Why can't a Python `set` alone do getRandom in O(1)?

- A. Sets can't hold ints
- B. Sets have no index, so picking a random member needs a copy into a list (O(n))
- C. random is slow
- D. Sets are sorted

**25.** *(String processing (1.8))* Longest Common Prefix: one pass of the OUTER loop should be

- A. one word
- B. one character position (column)
- C. one pair of words
- D. one letter of the alphabet

**26.** *(String processing (1.8))* Substring search: haystack length 10, needle length 4. Last start index worth trying?

- A. 10
- B. 9
- C. 6
- D. 7

**27.** *(String processing (1.8))* Roman to Integer: `"XC"` equals

- A. 110
- B. 90
- C. 100
- D. -90

**28.** *(String processing (1.8))* Zigzag with num_rows = 1 should return

- A. the string reversed
- B. the string unchanged
- C. an empty string
- D. an error

**29.** *(String processing (1.8))* Text Justification: 7 spaces over 3 gaps. Spaces per gap, left to right?

- A. 2, 2, 3
- B. 3, 2, 2
- C. 2, 3, 2
- D. 3, 3, 1

**30.** *(Picking the pattern)* "Return k after removing every 0 in place, keeping order." Best pattern?

- A. Prefix sums
- B. Read/write pointers
- C. Boyer–Moore
- D. Sorting

**31.** *(Picking the pattern)* "For each index, the largest value anywhere to its right." Best pattern?

- A. Suffix pass (right to left, running max)
- B. Two nested loops
- C. Binary search
- D. Counting

**32.** *(Picking the pattern)* "Biggest a[j] − a[i] with i < j." Best pattern?

- A. Sort then subtract ends
- B. Best-so-far scan tracking the minimum
- C. Counter
- D. Reversal

