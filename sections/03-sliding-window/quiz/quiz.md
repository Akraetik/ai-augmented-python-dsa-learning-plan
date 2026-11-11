# Section 03 · Sliding Window Checkpoint

22 questions · pass mark 85% · no notes, no IDE, no AI. Answers: [quiz_answers.md](quiz_answers.md). Better: open `quiz.html` in a browser for instant scoring by topic.

**1.** *(Fixed-size windows (3.1))* A fixed window of size k slides one step. How many items does the update touch?

- A. k
- B. 2: one enters, one leaves
- C. 1
- D. n

**2.** *(Fixed-size windows (3.1))* When `nums[right]` enters a window of size k, which item leaves?

- A. nums[right - 1]
- B. nums[right - k]
- C. nums[right - k + 1]
- D. nums[k]

**3.** *(Fixed-size windows (3.1))* Big-O of summing every window of size k from scratch?

- A. O(n)
- B. O(n · k)
- C. O(k)
- D. O(n log n)

**4.** *(Fixed-size windows (3.1))* Permutation in String: what must match between the window and s1?

- A. The first letter
- B. The sorted order
- C. The letter counts
- D. The length only

**5.** *(Longest valid window (3.2))* A window runs from left = 3 to right = 7. Its length?

- A. 4
- B. 5
- C. 7
- D. 10

**6.** *(Longest valid window (3.2))* Longest-valid template: where do you record the answer?

- A. Inside the while, before shrinking
- B. After the while, once the window is valid
- C. Before adding s[right]
- D. Only at the end

**7.** *(Longest valid window (3.2))* Why shrink with `while` and not `if`?

- A. It's faster
- B. One step left may not fix the window
- C. if is not allowed in loops
- D. No reason

**8.** *(Longest valid window (3.2))* The variable window has a while inside a for. Why is it still O(n)?

- A. The while rarely runs
- B. left only moves forward, so it moves at most n times in total
- C. Python optimizes it
- D. It isn't O(n)

**9.** *(Longest valid window (3.2))* Longest substring without repeats in `"abba"`?

- A. 1
- B. 2
- C. 3
- D. 4

**10.** *(Longest valid window (3.2))* Max Consecutive Ones III restated as a window rule:

- A. Window of all ones
- B. Longest window with at most k zeros
- C. Shortest window with k ones
- D. Window of size k

**11.** *(Longest valid window (3.2))* Window "AABAB", k = 1. Is it valid?

- A. Yes
- B. No

**12.** *(Shortest valid window (3.3))* Shortest-valid template: when does the while loop run?

- A. While the window is broken
- B. While the window is valid
- C. Once per step
- D. Never

**13.** *(Shortest valid window (3.3))* Shortest-valid: what should best start at?

- A. 0
- B. 1
- C. infinity
- D. len(nums)

**14.** *(Shortest valid window (3.3))* Minimum Size Subarray Sum: no window reaches the target. Return?

- A. infinity
- B. -1
- C. 0
- D. len(nums)

**15.** *(Shortest valid window (3.3))* Why does Minimum Size Subarray Sum need all positive numbers?

- A. To avoid overflow
- B. So growing raises the sum and shrinking lowers it
- C. So the list is sorted
- D. It doesn't

**16.** *(Shortest valid window (3.3))* Minimum Window Substring: when does `have` go up by one?

- A. Every time a letter of t enters
- B. When a letter's window count reaches exactly what t needs
- C. When the window grows
- D. When left moves

**17.** *(Shortest valid window (3.3))* Minimum Window Substring returns the substring. What must you record?

- A. Only the length
- B. The start index and the length
- C. Only the start
- D. The whole Counter

**18.** *(Word windows (3.4))* Concatenation of All Words with word length 4. How many separate window runs?

- A. 1
- B. 4
- C. len(words)
- D. len(s)

**19.** *(Word windows (3.4))* A piece that isn't any of the words enters the window. What now?

- A. Skip it, keep the window
- B. Clear the window and restart after it
- C. Shrink one step
- D. Return []

**20.** *(Picking the pattern)* "Longest subarray with sum ≤ k. Numbers can be negative." Sliding window?

- A. Yes, longest-valid template
- B. No: negatives break it
- C. Yes, fixed window
- D. Yes, shortest-valid

**21.** *(Picking the pattern)* "For each block of 7 days, the max temperature." Best pattern?

- A. Fixed window of size 7
- B. Two pointers from the ends
- C. Variable window
- D. Sort first

**22.** *(Picking the pattern)* "Sorted list. Find a pair that sums to target." Sliding window or two pointers?

- A. Sliding window
- B. Two pointers from the ends (Section 02)
- C. Fixed window of 2
- D. Counting

