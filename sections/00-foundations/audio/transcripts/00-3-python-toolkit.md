# 00-3 The Python Toolkit

**Narrator:** Section zero, track three. The Python toolkit.

**Narrator:** This track covers the parts of Python that show up in almost every interview problem. Lists. Strings. Loops. Dictionaries. Sets. And a few power tools.

**Narrator:** You'll hear questions. Answer them out loud before the answer voice does.

*[pause 1s]*

**Narrator:** Start with lists. A list holds items in order. Each item sits at a position, called an index. The first index is zero. Not one. Zero.

**Narrator:** A list of four items has indexes zero, one, two, and three. The last index is always the length minus one.

**Narrator:** Python also lets you count from the end. Index negative one is the last item. Negative two is the one before it.

**Narrator:** Question. A list has five items. What's the last valid index?

*[pause 3s]*

**Answer:** Four. The length minus one.

*[pause 1s]*

**Narrator:** Now the most important idea in this track. Index versus value.

**Narrator:** The index is the position. The value is the thing sitting at that position.

**Narrator:** If you loop with for x in the list, x is a value. If you loop with for i in range of the length, i is an index. If you need both, use enumerate. It hands you the index and the value together.

**Narrator:** The classic bug is taking a value and using it as if it were a position. Your mistake log calls that M one.

**Narrator:** Here's the check. Every time you write square brackets, ask: is the thing inside a position? Or is it a thing at a position?

*[pause 1s]*

**Narrator:** Changing lists. Append adds to the end. Fast. Pop with no number removes from the end. Fast. Pop zero removes from the front. Slow, because everything shifts.

**Narrator:** To swap two items, Python has a neat trick. Write the two positions on the left, and the same two positions in the opposite order on the right. Python swaps them in one line. You'll do this hundreds of times in this course.

*[pause 1s]*

**Narrator:** Slicing. A slice takes a piece of a list. You give a start and a stop. The stop is not included.

**Narrator:** Question. A list holds ten, twenty, thirty, forty. You slice from one to three. What do you get?

*[pause 3s]*

**Answer:** Twenty and thirty. Index one and index two. Index three is the stop, so it's left out.

**Narrator:** A slice with two colons and negative one reverses. It gives you a reversed copy.

**Narrator:** And remember, a slice makes a copy. That costs time. Don't slice inside a loop if you can avoid it.

*[pause 1s]*

**Narrator:** A trap with lists of lists. If you want a grid, three rows of three zeros, you might multiply a row by three. Don't. That gives you the same row three times. Change one, and all three change.

**Narrator:** Build the grid with a comprehension instead. One fresh row for each pass. You'll need this in the matrix section.

*[pause 1s]*

**Narrator:** Now strings. A string reads like a list. You can index it, slice it, loop over it, and ask its length.

**Narrator:** But you can't change it. Strings are immutable. To change a string, you build a new one.

**Narrator:** Question. What's the fast way to build a long string in a loop?

*[pause 3s]*

**Answer:** Append the pieces to a list. Then join them once, at the end.

**Narrator:** Right. Adding strings with plus inside a loop builds a new string every time. Joining once is linear.

*[pause 1s]*

**Narrator:** String tools you'll use constantly.

**Narrator:** Split, with nothing inside the parentheses, breaks a string into words. It splits on any run of spaces and drops the empty bits. That makes it perfect for messy input with extra spaces.

**Narrator:** Join glues a list of strings back together. Space dot join puts single spaces between the words.

**Narrator:** Strip trims spaces off both ends.

**Narrator:** Lower and upper change case.

**Narrator:** Is alpha asks: is this a letter? Is digit asks: is this a digit? Is al num asks: is this a letter or a digit?

**Narrator:** And two functions turn characters into numbers. Ord gives a character's number. Chr goes back.

**Narrator:** The trick: ord of a letter, minus ord of lowercase a, turns a into zero, b into one, and so on up to twenty five. That lets you use letters as list positions.

**Narrator:** Question. Ord of lowercase d minus ord of lowercase a. What is it?

*[pause 3s]*

**Answer:** Three.

*[pause 1s]*

**Narrator:** Loops. Use for when you know what you're walking through. Use while when you move by your own rules. Two pointers use while.

**Narrator:** Range takes a start, a stop, and a step. Like slicing, the stop is never included.

**Narrator:** Question. Range of two, ten, three. Which numbers?

*[pause 3s]*

**Answer:** Two, five, eight.

**Narrator:** Here's a bug that hangs programs. Inside a while loop, you write left plus one on its own line. That computes a number and throws it away. Left never moves. The loop runs forever.

**Narrator:** You need left plus equals one. That saves the result. Your log calls this M four. Every pointer move needs an equals sign.

*[pause 1s]*

**Narrator:** Returning from a loop. Say you're checking if every number is positive. As soon as you see a bad one, you can return false. But you can't return true until you've checked them all.

**Narrator:** So, false answers can return early, inside the loop. True answers usually wait until after the loop. That's M seven.

*[pause 1s]*

**Narrator:** Now dictionaries and sets. These are the most important tools for speed.

**Narrator:** A set holds unique items. No order. No duplicates. And checking if something is in a set is O of one.

**Narrator:** Here's the trigger. Whenever a problem makes you ask, have I seen this before, reach for a set.

**Narrator:** One gotcha. Empty curly braces make an empty dictionary, not a set. For an empty set, write set with empty parentheses.

*[pause 1s]*

**Narrator:** A dictionary maps keys to values. Looking up a key is O of one.

**Narrator:** Counting is the classic use. For each item, set its count to its current count plus one. Use get with a default of zero, so a new key doesn't crash.

**Narrator:** The other classic use is remembering where you saw something. Map each value to its index.

**Narrator:** Question. In Two Sum, you walk the list. Standing on a number x, what do you look up in the dictionary?

*[pause 3s]*

**Answer:** Target minus x. The partner you need. If it's there, you've found the pair.

**Narrator:** And what does the dictionary map from, and to?

*[pause 3s]*

**Answer:** From each value you've already passed, to its index.

*[pause 1s]*

**Narrator:** Keys must be things that can't change. Numbers, strings, tuples. Not lists. If you need a pair as a key, use a tuple.

*[pause 1s]*

**Narrator:** The power tools live in the collections module.

**Narrator:** Counter counts everything in one line. Two Counters can be compared directly. That makes anagram checks a one liner. Most common gives you the top items.

**Narrator:** Default dict is a dictionary with an automatic starting value. A default dict of list lets you append to a key that doesn't exist yet. Great for grouping.

**Narrator:** Deque, spelled d e q u e, is a list that's fast at both ends. Use it as a queue. Pop left is O of one.

*[pause 1s]*

**Narrator:** Sorting. Sorted, the function, gives you a new sorted list. Dot sort, the method, sorts the list in place and returns None.

**Narrator:** That last part bites people. If you write x equals my list dot sort, x becomes None.

**Narrator:** You can sort by any rule with key. Key equals len sorts words by length. Reverse equals true sorts big to small.

**Narrator:** Sorting costs n log n. Very often, sorting first turns a hard problem into an easy one.

*[pause 1s]*

**Narrator:** A few number facts. Double slash is integer division. It drops the remainder. Percent gives the remainder.

**Narrator:** Percent two equals zero means even. Index percent n wraps an index around a list of length n. You'll use that in Rotate Array.

**Narrator:** Float infinity is bigger than any number. It's a good starting value when you're hunting for a minimum.

**Narrator:** And Python integers never overflow. Other languages make you worry about that. You don't have to.

*[pause 1s]*

**Narrator:** Quick fire. Name the tool.

**Narrator:** Have I seen this before?

*[pause 2s]*

**Answer:** A set.

**Narrator:** How many times does each letter appear?

*[pause 2s]*

**Answer:** Counter. Or a dictionary with get.

**Narrator:** Group words by their sorted letters.

*[pause 2s]*

**Answer:** A default dict of list.

**Narrator:** Take items from the front of a line, over and over.

*[pause 2s]*

**Answer:** A deque, with pop left.

**Narrator:** Index and value in the same loop.

*[pause 2s]*

**Answer:** Enumerate.

**Narrator:** Build a string from many pieces.

*[pause 2s]*

**Answer:** A list, then join.

*[pause 1s]*

**Narrator:** That's the toolkit. Next track is a rapid fire drill. Put it on repeat.
