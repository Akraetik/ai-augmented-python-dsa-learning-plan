# Section 00 · Diagnostic and Checkpoint

26 questions · pass mark 85% · no notes, no IDE, no AI. Answers: [quiz_answers.md](quiz_answers.md). Better: open `quiz.html` in a browser for instant scoring by topic.

**1.** *(How tests are graded)* A function prints the correct answer, but the grader marks every test wrong. Most likely cause?

- A. The grader is broken
- B. The function prints instead of returning, so it returns `None`
- C. Python 3 is required
- D. The function is too slow

**2.** *(How tests are graded)* A problem's signature ends in `-> None` and says "modify nums in place." What should your function do?

- A. Return a new sorted list
- B. Change the list it was given and return nothing
- C. Print the list
- D. Return `True` when done

**3.** *(Big-O)* Constraints say `1 <= n <= 10^5`. Which approach will likely time out?

- A. Sort, then one pass
- B. One pass with a set
- C. Two nested loops over all pairs
- D. One pass with two pointers

**4.** *(Big-O)* What is the time complexity?

```python
i = n
while i > 1:
    i = i // 2
```

- A. O(1)
- B. O(log n)
- C. O(n)
- D. O(n log n)

**5.** *(Big-O)* What is the time complexity? (`nums` is a list of length n.)

```python
for x in nums:
    if -x in nums:
        return True
```

- A. O(n)
- B. O(n log n)
- C. O(n^2)
- D. O(1)

**6.** *(Big-O)* Which operation is O(n) on a Python list of length n?

- A. `nums.append(5)`
- B. `nums[-1]`
- C. `nums.pop()`
- D. `nums.pop(0)`

**7.** *(Big-O)* You sort a list, then loop over it once. Overall time?

- A. O(n)
- B. O(n log n)
- C. O(n^2)
- D. O(n + log n)

**8.** *(Lists and indexing)* What does this print?

```python
nums = [10, 20, 30, 40]
print(nums[1:3], nums[-1])
```

- A. [20, 30] 40
- B. [20, 30, 40] 40
- C. [10, 20, 30] 10
- D. [20, 30] 30

**9.** *(Lists and indexing)* In `for x in nums:`, what is `x`?

- A. An index
- B. A value from the list
- C. The length
- D. A copy of the list

**10.** *(Lists and indexing)* What does this print?

```python
a = [1, 2]
b = a
b.append(3)
print(a)
```

- A. [1, 2]
- B. [1, 2, 3]
- C. [3]
- D. Error

**11.** *(Lists and indexing)* Which line correctly builds a 3x3 grid of zeros with independent rows?

- A. `[[0] * 3] * 3`
- B. `[0] * 9`
- C. `[[0] * 3 for _ in range(3)]`
- D. `[[0, 0, 0]] * 3`

**12.** *(Strings)* What does this print?

```python
s = "  the  sky is "
print(s.split())
```

- A. ['', 'the', '', 'sky', 'is', '']
- B. ['the', 'sky', 'is']
- C. ['the  sky is']
- D. ['  the', 'sky', 'is ']

**13.** *(Strings)* What's the fast way to build a long string in a loop?

- A. `out += piece` each time
- B. Append pieces to a list, then `''.join(parts)` once
- C. Use `out = out + piece`
- D. Convert to a set first

**14.** *(Strings)* What does `ord('e') - ord('a')` return?

- A. 4
- B. 5
- C. 'e'
- D. 101

**15.** *(Loops and returns)* What's wrong with this check for "all numbers are positive"?

```python
def all_pos(nums):
    for x in nums:
        if x > 0:
            return True
    return False
```

- A. Nothing
- B. It returns True after seeing ONE positive number
- C. It should use `while`
- D. `x > 0` should be `x >= 0`

**16.** *(Loops and returns)* What does this loop do?

```python
left, right = 0, 5
while left < right:
    left + 1
```

- A. Runs 5 times
- B. Runs forever
- C. Runs 0 times
- D. Raises an error

**17.** *(Loops and returns)* `range(2, 11, 3)` produces which numbers?

- A. 2, 5, 8, 11
- B. 2, 5, 8
- C. 3, 6, 9
- D. 2, 4, 6, 8, 10

**18.** *(Dicts and sets)* You need to answer "have I seen this value before?" many times. Best tool?

- A. A list and `in`
- B. A set
- C. Sorting each time
- D. A string

**19.** *(Dicts and sets)* What does this return?

```python
counts = {}
for ch in "abca":
    counts[ch] = counts.get(ch, 0) + 1
return counts
```

- A. {'a': 1, 'b': 1, 'c': 1}
- B. {'a': 2, 'b': 1, 'c': 1}
- C. ['a', 'b', 'c', 'a']
- D. KeyError

**20.** *(Dicts and sets)* In Two Sum, what does the dict store?

- A. index -> value
- B. value -> index of where you saw it
- C. value -> count
- D. target -> answer

**21.** *(Dicts and sets)* Why does `{[1, 2]}` raise an error?

- A. Sets can't hold numbers
- B. Lists are mutable, so they can't go in a set
- C. Sets need two items
- D. Missing a comma

**22.** *(collections and sorting)* Which is the quickest correct anagram check?

- A. `set(s) == set(t)`
- B. `Counter(s) == Counter(t)`
- C. `len(s) == len(t)`
- D. `s == t[::-1]`

**23.** *(collections and sorting)* What is `x` after this line?

```python
x = [3, 1, 2].sort()
```

- A. [1, 2, 3]
- B. [3, 1, 2]
- C. None
- D. Error

**24.** *(collections and sorting)* You need to remove from the front of a queue thousands of times. Use:

- A. `list.pop(0)`
- B. `collections.deque.popleft()`
- C. `list.remove(x)`
- D. Slicing `q = q[1:]`

**25.** *(Routine and debugging)* A test fails with `IndexError: list index out of range` inside `for i in range(len(nums)): ... nums[i + 1]`. Fix?

- A. Use `range(len(nums) - 1)`
- B. Use `range(len(nums) + 1)`
- C. Wrap it in try/except
- D. Sort first

**26.** *(Routine and debugging)* What should you do FIRST when you get a new problem?

- A. Start typing the code
- B. Restate it, work an example by hand, and note what it returns
- C. Look up the solution
- D. Write the fastest version you can think of

