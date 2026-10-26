# 00-4 Rapid Fire Drill

**Narrator:** Section zero, track four. Rapid fire drill.

**Narrator:** Questions come fast. You get a few seconds. Say your answer out loud. Then hear the right one.

**Narrator:** Missed one? That's the point. Put this track on repeat.

*[pause 2s]*

**Narrator:** What two things does every coding test grade?

*[pause 4s]*

**Answer:** Correctness, and performance.

**Narrator:** Your function prints the right answer, but fails every test. Why?

*[pause 4s]*

**Answer:** It printed instead of returning. The grader got None.

**Narrator:** The signature says it returns None. What should you do?

*[pause 4s]*

**Answer:** Change the input in place. Return nothing.

**Narrator:** Name four edge cases for a list problem.

*[pause 5s]*

**Answer:** Empty. One item. All the same. Negatives. And the maximum size.

**Narrator:** The Big O ladder, fastest to slowest.

*[pause 5s]*

**Answer:** One. Log n. n. n log n. n squared. Two to the n.

**Narrator:** Loops one after another. Add or multiply?

*[pause 3s]*

**Answer:** Add.

**Narrator:** A loop inside a loop. Add or multiply?

*[pause 3s]*

**Answer:** Multiply.

**Narrator:** A loop that halves n every pass.

*[pause 3s]*

**Answer:** O of log n.

**Narrator:** What does sorting cost?

*[pause 3s]*

**Answer:** O of n log n.

**Narrator:** n is up to one hundred thousand. What's your target?

*[pause 4s]*

**Answer:** O of n log n, or O of n.

**Narrator:** n is up to one thousand. Is a nested loop OK?

*[pause 3s]*

**Answer:** Yes. O of n squared is fine.

**Narrator:** n is twenty or less. What does that hint?

*[pause 4s]*

**Answer:** Try everything. Backtracking.

**Narrator:** Cost of checking if x is in a list?

*[pause 3s]*

**Answer:** O of n.

**Narrator:** Cost of checking if x is in a set?

*[pause 3s]*

**Answer:** O of one.

**Narrator:** Cost of pop zero on a list?

*[pause 3s]*

**Answer:** O of n. Use a deque.

**Narrator:** Cost of a slice of k items?

*[pause 3s]*

**Answer:** O of k. It copies.

**Narrator:** Cost of asking for a list's length?

*[pause 3s]*

**Answer:** O of one.

**Narrator:** What does space complexity measure?

*[pause 4s]*

**Answer:** Extra memory as the input grows. Not counting the input.

**Narrator:** Index versus value. Which is the position?

*[pause 3s]*

**Answer:** The index.

**Narrator:** Loop that gives you index and value together?

*[pause 3s]*

**Answer:** Enumerate.

**Narrator:** Last valid index of a list?

*[pause 3s]*

**Answer:** Length minus one.

**Narrator:** Does a slice include its stop index?

*[pause 3s]*

**Answer:** No.

**Narrator:** Does b equals a copy a list?

*[pause 3s]*

**Answer:** No. Both names point at the same list.

**Narrator:** Can you change a string in place?

*[pause 3s]*

**Answer:** No. Strings are immutable.

**Narrator:** Fast way to build a string in a loop?

*[pause 4s]*

**Answer:** Collect pieces in a list. Join once.

**Narrator:** Split with no arguments. What does it do with extra spaces?

*[pause 4s]*

**Answer:** Splits on any run of whitespace and drops the empties.

**Narrator:** How do you turn a letter into a number from zero to twenty five?

*[pause 4s]*

**Answer:** Ord of the letter, minus ord of a.

**Narrator:** Negative seven, integer divided by two.

*[pause 4s]*

**Answer:** Negative four. It rounds down.

**Narrator:** Trigger: have I seen this before?

*[pause 3s]*

**Answer:** Set.

**Narrator:** Trigger: frequency, or anagram.

*[pause 3s]*

**Answer:** Counter.

**Narrator:** Trigger: grouping things.

*[pause 3s]*

**Answer:** Default dict of list.

**Narrator:** Trigger: removing from the front, over and over.

*[pause 3s]*

**Answer:** Deque.

**Narrator:** Empty curly braces make what?

*[pause 3s]*

**Answer:** An empty dictionary. Not a set.

**Narrator:** Why can't a list be a dictionary key?

*[pause 4s]*

**Answer:** Lists can change, so they're not hashable. Use a tuple.

**Narrator:** What does dot sort return?

*[pause 3s]*

**Answer:** None. It sorts in place.

**Narrator:** Two Sum. Standing on x, what do you look up?

*[pause 4s]*

**Answer:** Target minus x.

**Narrator:** Two Sum. Why check the dictionary before adding x?

*[pause 4s]*

**Answer:** So x can't pair with itself.

**Narrator:** Running sum. How do you get each answer?

*[pause 4s]*

**Answer:** The previous answer, plus the current number.

**Narrator:** Mistake M one?

*[pause 3s]*

**Answer:** Index versus value.

**Narrator:** Mistake M four?

*[pause 3s]*

**Answer:** Calculating but not saving. Left plus one instead of left plus equals one.

**Narrator:** Mistake M five?

*[pause 3s]*

**Answer:** Off by one at the ends.

**Narrator:** Mistake M six?

*[pause 3s]*

**Answer:** Not reading the return type.

**Narrator:** Mistake M seven?

*[pause 3s]*

**Answer:** Returning true too early, inside the loop.

**Narrator:** When you're stuck, what question do you ask?

*[pause 4s]*

**Answer:** What work am I repeating?

**Narrator:** First step of the routine?

*[pause 3s]*

**Answer:** Restate the problem. And say what it returns.

**Narrator:** Last step of the routine?

*[pause 3s]*

**Answer:** Test it by tracing, line by line.

*[pause 1s]*

**Narrator:** End of the drill. Run it again tomorrow. When you can beat every answer, you're ready for the gate.
