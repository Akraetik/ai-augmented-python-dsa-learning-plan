# Section 02 · Two Pointers Checkpoint

22 questions · pass mark 85% · no notes, no IDE, no AI. Answers: [quiz_answers.md](quiz_answers.md). Better: open `quiz.html` in a browser for instant scoring by topic.

**1.** *(Opposite ends (2.1))* Why does an opposite-ends two-pointer loop run in O(n)?

- A. It sorts first
- B. Each step discards at least one item
- C. It uses a dict
- D. It stops halfway

**2.** *(Opposite ends (2.1))* Two Sum II on a sorted list: the current sum is too SMALL. What do you do?

- A. right -= 1
- B. left += 1
- C. Move both
- D. Restart from the ends

**3.** *(Opposite ends (2.1))* Why is it safe to discard `numbers[left]` when the sum is too small?

- A. It's the smallest number
- B. Even the biggest remaining partner, `numbers[right]`, isn't enough
- C. Sorted lists have no duplicates
- D. It was already used

**4.** *(Opposite ends (2.1))* Two Sum II finds the pair at indexes 0 and 3. What do you return?

- A. [0, 3]
- B. [1, 4]
- C. [0, 4]
- D. [3, 0]

**5.** *(Opposite ends (2.1))* Valid Palindrome on `".,!"` (all punctuation). The inner skip loop has no `left < right` check. What happens?

- A. Returns True
- B. Returns False
- C. `left` runs past the end: IndexError
- D. Infinite loop

**6.** *(Opposite ends (2.1))* Squares of `[-6, -2, 1, 5]` in O(n). Which square goes into the LAST output slot first?

- A. 25
- B. 36
- C. 1
- D. 4

**7.** *(Same direction (2.2))* Is Subsequence: which pointer moves on every step?

- A. The one in s
- B. The one in t
- C. Both, always
- D. Neither

**8.** *(Same direction (2.2))* Is `"aec"` a subsequence of `"abcde"`?

- A. Yes
- B. No

**9.** *(Same direction (2.2))* Is the empty string a subsequence of `"xyz"`?

- A. Yes
- B. No

**10.** *(Shrink the weaker side (2.3))* Container: lines of height 6 at index 2 and height 9 at index 7. Area?

- A. 30
- B. 45
- C. 54
- D. 15

**11.** *(Shrink the weaker side (2.3))* Container: left line is height 3, right line is height 10. Which pointer moves?

- A. right
- B. left
- C. both
- D. neither, stop

**12.** *(Shrink the weaker side (2.3))* Why can moving the TALLER line never help?

- A. It can, sometimes
- B. The short line still caps the level, and the width shrinks
- C. Taller lines hold no water
- D. It breaks sorting

**13.** *(Sort + two pointers / 3Sum (2.4))* 3Sum: after sorting and fixing `nums[i]`, what's left to solve?

- A. Binary search for one number
- B. Two Sum II on the rest, for −nums[i]
- C. Another 3Sum
- D. A prefix sum

**14.** *(Sort + two pointers / 3Sum (2.4))* 3Sum: which skip keeps `[-1, -1, 2]` while avoiding duplicate fixed values?

- A. skip if nums[i] == nums[i + 1]
- B. skip if i > 0 and nums[i] == nums[i - 1]
- C. skip if nums[i] < 0
- D. no skip

**15.** *(Sort + two pointers / 3Sum (2.4))* 3Sum on `[-2, 0, 0, 2, 2]`. After recording `[-2, 0, 2]`, what must happen before the next check?

- A. Stop the loop
- B. Move left past both 0s and right past both 2s
- C. Move only left
- D. Reset left and right

**16.** *(Sort + two pointers / 3Sum (2.4))* 3Sum: the fixed number `nums[i]` is 5 (list sorted). What do you do?

- A. Continue
- B. Break: everything after it is positive
- C. Skip one
- D. Reverse the list

**17.** *(Sort + two pointers / 3Sum (2.4))* Big-O of 3Sum with sort + two pointers?

- A. O(n log n)
- B. O(n²)
- C. O(n³)
- D. O(n)

**18.** *(O(1)-space water (2.5))* Two-pointer water: left_max = 3, right_max = 7. Which side's water level is known for sure?

- A. left
- B. right
- C. both
- D. neither

**19.** *(O(1)-space water (2.5))* What does the two-pointer water solution save compared to the prefix/suffix version?

- A. Time: O(n) → O(log n)
- B. Space: O(n) → O(1)
- C. Nothing
- D. It handles negatives

**20.** *(Picking the pattern)* "Sorted list. Count pairs whose sum is below k." Best pattern?

- A. Opposite-ends two pointers
- B. Prefix sum
- C. Boyer–Moore
- D. Sliding window

**21.** *(Picking the pattern)* "Merge two sorted lists into a new sorted list." Best pattern?

- A. Same-direction pointers, one per list
- B. Opposite ends
- C. Sort the concatenation only
- D. Counting

**22.** *(Picking the pattern)* "Is this string a palindrome if you may delete at most one character?" First tool?

- A. Opposite-ends pointers; on a mismatch, try skipping either side once
- B. Counter
- C. Sorting
- D. Prefix sums

