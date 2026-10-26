# 01-3 Reach, Prefix and Suffix, Design

**Narrator:** Section one, track three. Reach, prefix and suffix passes, and design. Lessons one point five through one point seven.

*[pause 1s]*

**Narrator:** Jump Game. Each number says the most you can jump forward from that spot. Can you reach the last index?

**Narrator:** What single number do you track?

*[pause 3s]*

**Answer:** Reach. The farthest index you could get to so far.

**Narrator:** How do you update it?

*[pause 4s]*

**Answer:** At each index, reach becomes the bigger of reach, and the index plus its jump.

**Narrator:** When are you stuck?

*[pause 3s]*

**Answer:** When you're standing on an index bigger than reach. You could never have gotten there.

**Narrator:** When have you made it?

*[pause 4s]*

**Answer:** When reach is at least the last index. That's the length minus one, not the length.

*[pause 1s]*

**Narrator:** Try one in your head. Two, zero, zero, one. Can you reach the end?

*[pause 6s]*

**Answer:** No. From index zero, reach is two. Indexes one and two are zeros, so reach stays at two. Index three is past reach. Stuck.

*[pause 1s]*

**Narrator:** Jump Game two. The end is always reachable. Find the fewest jumps.

**Narrator:** Think in rings. With zero jumps, you stand on index zero. With one jump, you can stand anywhere the first jump reaches. That's ring one.

**Narrator:** Name the three variables.

*[pause 5s]*

**Answer:** The jump count. Where the current ring ends. And the farthest the next ring can reach.

**Narrator:** When do you add a jump?

*[pause 4s]*

**Answer:** When your index reaches the end of the current ring. Then the ring end becomes the farthest.

**Narrator:** Why loop only to the second to last index?

*[pause 4s]*

**Answer:** Once you're on the last index, you don't need another jump. Looping onto it can count one extra.

**Narrator:** This is breadth first search in disguise. You'll see it for real in the graph sections.

*[pause 1s]*

**Narrator:** Gas Station. Stations in a circle. Each gives gas, each drive costs gas. Find the start.

**Narrator:** Fact one. When is the answer minus one?

*[pause 4s]*

**Answer:** When total gas is less than total cost.

**Narrator:** Fact two. You start at station two, and run dry trying to reach station six. Could stations three, four, or five work as a start?

*[pause 6s]*

**Answer:** No. You arrived at each of them with zero or more gas. Starting there means starting with zero. That's never better. So they'd fail too.

**Narrator:** So where do you try next?

*[pause 3s]*

**Answer:** Station seven. One past where you ran dry.

**Narrator:** And that's the whole algorithm. Check the totals. Walk once. Reset the start whenever the tank goes negative.

*[pause 1s]*

**Narrator:** Prefix and suffix passes. The idea: when an answer depends on everything to the left and everything to the right, sweep once in each direction.

**Narrator:** Product of Array Except Self. For each index, the product of every other number. No division.

**Narrator:** Why no division?

*[pause 4s]*

**Answer:** Zeros. You can't divide by zero, and one or two zeros need special handling.

**Narrator:** Split "everything except i" into two parts. What are they?

*[pause 4s]*

**Answer:** Everything to the left of i. And everything to the right of i.

**Narrator:** For two, three, four, what's the left products row?

*[pause 5s]*

**Answer:** One, two, six. The empty product is one.

**Narrator:** And the right products row?

*[pause 5s]*

**Answer:** Twelve, four, one.

**Narrator:** So the answer?

*[pause 5s]*

**Answer:** Twelve, eight, six.

**Narrator:** Here's a detail that matters. In the prefix loop, do you record first, then include the current number? Or include first, then record?

*[pause 5s]*

**Answer:** Record first. Then include. That way index i is never part of its own product.

*[pause 1s]*

**Narrator:** Trapping Rain Water. Bars of different heights. How much water sits between them?

**Narrator:** Focus on one bar. What decides how high the water rises above it?

*[pause 5s]*

**Answer:** The shorter of two walls. The tallest bar on its left, and the tallest bar on its right.

**Narrator:** So water above that bar equals?

*[pause 4s]*

**Answer:** The smaller of those two maximums, minus the bar's own height.

**Narrator:** What do you precompute?

*[pause 4s]*

**Answer:** The running max from the left, and the running max from the right. Two sweeps.

**Narrator:** You'll solve this one again in the next section with two pointers and no extra lists.

*[pause 1s]*

**Narrator:** Candy. Kids in a line with ratings. Each gets at least one. A higher rated kid gets more than a lower rated neighbor.

**Narrator:** Why two sweeps?

*[pause 4s]*

**Answer:** There are two rules. One about the left neighbor. One about the right. Each sweep handles one.

**Narrator:** In the second sweep, why use max instead of just setting the value?

*[pause 5s]*

**Answer:** Plain setting could lower a number the first sweep needed. Max keeps both rules true.

**Narrator:** Ratings one, zero, two. How much candy?

*[pause 5s]*

**Answer:** Five. Two, one, two.

*[pause 1s]*

**Narrator:** Design. Insert Delete Get Random, all in constant time.

**Narrator:** Why not just use a set?

*[pause 4s]*

**Answer:** A set has no positions. Picking a random member means copying it to a list first. That's linear.

**Narrator:** Why not just a list?

*[pause 4s]*

**Answer:** Finding and removing from the middle of a list is linear.

**Narrator:** So what do you store?

*[pause 4s]*

**Answer:** A list of the values. And a dictionary from each value to its position in the list.

**Narrator:** Walk through remove.

*[pause 8s]*

**Answer:** Look up the value's position. Take the last value in the list. Put it in that position. Update the last value's position in the dictionary. Pop the end of the list. Delete the removed value from the dictionary.

**Narrator:** What's the most common bug?

*[pause 4s]*

**Answer:** Forgetting to update the moved value's position in the dictionary.

**Narrator:** And what if the value you remove is the last one in the list?

*[pause 5s]*

**Answer:** The steps still work. It overwrites itself, then gets popped and deleted.

*[pause 1s]*

**Narrator:** One more new problem. For each day, find the warmest temperature on any later day. Which pattern?

*[pause 5s]*

**Answer:** A suffix pass. Sweep right to left with a running max.

*[pause 1s]*

**Narrator:** That's reach, prefix and suffix, and design. Next track: strings.
