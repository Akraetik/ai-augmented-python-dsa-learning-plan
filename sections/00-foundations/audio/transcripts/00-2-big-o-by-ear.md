# 00-2 Big O by Ear

**Narrator:** Section zero, track two. Big O, by ear.

**Narrator:** When you hear a question, try to answer it before the answer voice does. Say it out loud if you can. That's the practice.

*[pause 1s]*

**Narrator:** Big O answers one question. When the input gets bigger, how much more work does the code do?

**Narrator:** It does not measure seconds. Seconds depend on the computer. Big O measures growth.

**Narrator:** We call the size of the input n. For a list, n is how many items it holds. For a string, how many characters.

*[pause 1s]*

**Narrator:** The fastest kind of code is O of one. Constant time. The work is the same no matter how big the input gets.

**Narrator:** Grabbing the first item of a list is O of one. Looking up a key in a dictionary is O of one. Ten items or ten million, same work.

*[pause 1s]*

**Narrator:** Next is O of n. Linear time. Double the input, double the work.

**Narrator:** One loop over the list is O of n. Adding up every number. Finding the biggest. Counting how many are even.

*[pause 1s]*

**Narrator:** Then O of n squared. Quadratic. Double the input, four times the work.

**Narrator:** This comes from a loop inside a loop. For each item, you look at every other item. Checking every pair.

**Narrator:** At a hundred items, that's ten thousand steps. Fine. At a hundred thousand items, that's ten billion steps. Not fine.

*[pause 1s]*

**Narrator:** Here's a rule you'll use constantly. Loops one after another add. Loops inside each other multiply.

**Narrator:** Two separate loops over the list. One, then the other. What's the Big O?

*[pause 3s]*

**Answer:** O of n. n plus n is two n, and we drop the two.

**Narrator:** One loop, and inside it, another loop over the whole list. What's the Big O?

*[pause 3s]*

**Answer:** O of n squared. n times n.

**Narrator:** One loop over the list, and inside it, a loop that always runs ten times. What's the Big O?

*[pause 3s]*

**Answer:** O of n. Ten is a constant. n times ten is still linear.

*[pause 1s]*

**Narrator:** Now the one that surprises people. O of log n.

**Narrator:** Picture a loop that cuts the problem in half every time. A million becomes five hundred thousand. Then two hundred fifty thousand. And so on.

**Narrator:** How many halvings until you reach one? About twenty. Only twenty steps for a million items.

**Narrator:** That's O of log n. Logarithmic. It grows so slowly it's almost free.

**Narrator:** Binary search works this way. You look at the middle of a sorted list, throw away the half that can't hold your answer, and repeat.

**Narrator:** The rule. If the problem gets cut in half each step, think log n.

*[pause 1s]*

**Narrator:** And then O of n log n. This is the cost of sorting. Python's sort is n log n.

**Narrator:** It's a little worse than linear. Much better than quadratic. If you sort the list once and then loop over it once, the total is n log n. The sort is the bigger cost, so it wins.

*[pause 1s]*

**Narrator:** Here's the ladder. Fastest to slowest. Say it with me.

**Narrator:** O of one. O of log n. O of n. O of n log n. O of n squared. O of two to the n.

*[pause 2s]*

**Narrator:** One more time, and this time try to say it before you hear it.

*[pause 4s]*

**Answer:** O of one. O of log n. O of n. O of n log n. O of n squared. O of two to the n.

*[pause 1s]*

**Narrator:** Now the most useful skill in this track. Reading the constraints.

**Narrator:** Every problem tells you how big the input can get. Something like: the list has between one and one hundred thousand items.

**Narrator:** That number tells you what Big O you need. Before you write a line.

**Narrator:** Python does roughly ten to fifty million simple steps per second. The grader gives you about a second or two.

**Narrator:** So. If n is at most one thousand, what Big O is fine?

*[pause 3s]*

**Answer:** O of n squared is fine. A million steps.

**Narrator:** If n is up to one hundred thousand, what do you need?

*[pause 3s]*

**Answer:** O of n log n or O of n. No loop inside a loop over all pairs.

**Narrator:** If n is twenty or less, what does that hint?

*[pause 3s]*

**Answer:** You can try every possibility. Exponential is OK. That's backtracking.

**Narrator:** If n is up to a billion?

*[pause 3s]*

**Answer:** O of log n or O of one. Math or binary search. You can't even loop once.

*[pause 1s]*

**Narrator:** Next. Hidden loops. These are lines of Python that look like one step but are secretly a loop. They cause most of the "too slow" failures you'll see.

**Narrator:** Checking if something is in a list. The word in, followed by a list. Python checks every item, one by one. That's O of n.

**Narrator:** Checking if something is in a set, or in a dictionary. That's O of one. Python jumps straight to it.

**Narrator:** So here's a question. You loop over a list, and inside the loop, you check if some value is in the same list. What's the real Big O?

*[pause 3s]*

**Answer:** O of n squared. The in check on a list is a hidden loop, inside the visible loop.

**Narrator:** And the fix?

*[pause 3s]*

**Answer:** Turn the list into a set once, before the loop. Then each check is O of one, and the whole thing is O of n.

*[pause 1s]*

**Narrator:** More hidden loops. Removing the first item of a list, with pop zero, shifts everything else left. O of n. Removing the last item, with plain pop, is O of one.

**Narrator:** If you need to remove from the front over and over, use a deque from the collections module. Its pop left is O of one.

**Narrator:** Slicing a list makes a copy. Copying k items costs O of k. Fine once. Bad inside a loop.

**Narrator:** Sum, max, and min each scan the whole list. O of n. Call one inside a loop and you've built O of n squared without noticing.

**Narrator:** Length is the exception. Asking a list for its length is O of one. Python keeps track.

**Narrator:** Adding strings together with plus makes a brand new string each time. In a loop, that adds up. Collect the pieces in a list, and join them once at the end.

*[pause 1s]*

**Narrator:** Quick fire. Is it fast or slow? Answer before you hear it.

**Narrator:** Checking if x is in a set.

*[pause 2s]*

**Answer:** Fast. O of one.

**Narrator:** Checking if x is in a list.

*[pause 2s]*

**Answer:** Slow. O of n.

**Narrator:** Pop from the end of a list.

*[pause 2s]*

**Answer:** Fast. O of one.

**Narrator:** Pop from the front of a list.

*[pause 2s]*

**Answer:** Slow. O of n. Use a deque.

**Narrator:** Append to a list.

*[pause 2s]*

**Answer:** Fast. O of one, on average.

**Narrator:** Sorting a list.

*[pause 2s]*

**Answer:** O of n log n.

**Narrator:** Calling sum on a list inside a loop over that list.

*[pause 2s]*

**Answer:** Slow. O of n squared.

*[pause 1s]*

**Narrator:** Last idea. Space complexity. Same idea as time, but for memory.

**Narrator:** How much extra memory does your code use as the input grows? Don't count the input itself.

**Narrator:** A handful of variables is O of one space. Building a set or a new list that can hold every item is O of n space.

**Narrator:** When a problem says in place, or constant extra space, it means: don't build a new list. Change the one you were given. Use a few variables.

**Narrator:** There's often a trade. A set uses O of n memory to save you O of n squared time. That trade is usually worth it. Interviewers like it when you say the trade out loud.

*[pause 1s]*

**Narrator:** That's Big O. Next track: the Python toolkit. The lists, strings, dictionaries, and sets you'll use in every problem.
