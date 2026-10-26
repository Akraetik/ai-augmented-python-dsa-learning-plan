# 01-1 Array and String Primer

**Narrator:** Section one, track one. Arrays and strings. The primer.

**Narrator:** Listen to this before you open the first lesson. Don't try to memorize it. You're just loading the words, so the lessons feel familiar.

*[pause 1s]*

**Narrator:** This section has twenty four problems from the Leet Code Top Interview one fifty. They look different. They're not. They use seven patterns. Learn the seven, and the twenty four become variations.

**Narrator:** Here they are, one at a time.

*[pause 1s]*

**Narrator:** Pattern one. Read and write pointers.

**Narrator:** You have a list. You need to remove some items, in place, and report how many you kept.

**Narrator:** You use two positions. Read walks every item. Write marks the next empty slot for a keeper. When read finds an item worth keeping, it copies it to write, and write moves forward one.

**Narrator:** Read is always at or ahead of write. So you never overwrite something you haven't looked at yet.

**Narrator:** The trigger words are: in place. Return k. The first k elements.

**Narrator:** Four problems use this. Remove Element. Remove Duplicates. Remove Duplicates two. And Merge Sorted Array, which runs the same idea backward, from the end of the list.

*[pause 1s]*

**Narrator:** Pattern two. Counting, and voting.

**Narrator:** Some problems are easy once you count. How many times does each value appear? A Counter answers that in one line.

**Narrator:** Majority Element asks for the value that fills more than half the list. Counting solves it. But there's a famous trick that uses no extra memory. It's called Boyer Moore voting.

**Narrator:** Picture a room. Pair off two people holding different signs and send both home. Keep going. The majority has more than half the room, so it can't all be paired away. Whoever's left holds the majority sign.

**Narrator:** The other problem here is H Index. Sort the numbers biggest first. Then compare each value to its position. The picture tells you the answer.

*[pause 1s]*

**Narrator:** Pattern three. Index math.

**Narrator:** Rotate Array shifts every item k places to the right, and the items that fall off the end wrap to the front.

**Narrator:** The tool is modulo. The percent sign. Position i moves to i plus k, mod n. Modulo turns "past the end" into "back at the start."

**Narrator:** And before anything else, shrink k. Rotating by the full length changes nothing. So k mod n is all you need.

**Narrator:** For the no extra memory version, there's a trick. Reverse the whole list. Then reverse the first k. Then reverse the rest. Done.

*[pause 1s]*

**Narrator:** Pattern four. The best so far scan.

**Narrator:** Best Time to Buy and Sell Stock. Buy one day, sell a later day. Biggest profit.

**Narrator:** The slow way checks every pair. The fast way walks once and remembers the lowest price so far. At each day, ask: if I sell today, what's my profit? Keep the best.

**Narrator:** The second version lets you trade as often as you like. Then the answer is even simpler. Add up every day where the price went up from the day before.

*[pause 1s]*

**Narrator:** Pattern five. Reach.

**Narrator:** Jump Game. Each number says how far you may jump. Can you reach the end?

**Narrator:** Don't try every path. Track one number: the farthest index you could reach so far. If you ever stand somewhere past that, you're stuck.

**Narrator:** Jump Game two asks for the fewest jumps. Think in rings. Everything you can reach in one jump is ring one. Everything from there in one more is ring two. Count rings.

**Narrator:** Gas Station fits here too. A circle of stations. Find where to start. The trick is a reset. When your tank goes negative, no station since your start can work. So start fresh at the next one.

*[pause 1s]*

**Narrator:** Pattern six. Prefix and suffix passes.

**Narrator:** Some answers depend on everything to the left and everything to the right. Product of Array Except Self is the classic. For each spot, multiply everything except that spot. No division allowed.

**Narrator:** Split it in two. Everything to the left. Everything to the right. One sweep left to right. One sweep right to left. Multiply.

**Narrator:** Trapping Rain Water uses the same two sweeps. Water above a bar is limited by the shorter of the tallest bar on its left and the tallest bar on its right.

**Narrator:** Candy uses two sweeps too. One for the left neighbor rule. One for the right.

*[pause 1s]*

**Narrator:** Pattern seven. Design with two structures.

**Narrator:** Insert Delete Get Random asks you to build a class where every operation is constant time.

**Narrator:** A list gives you random picks. A dictionary gives you fast lookups. Neither does everything. So use both. The dictionary maps each value to its position in the list.

**Narrator:** The clever part is delete. Removing from the middle of a list is slow. Removing from the end is fast. So swap the doomed item with the last one, then pop the end.

*[pause 1s]*

**Narrator:** And then strings. Eight problems. Strings are lists you can't change. You read them like lists. You build new ones with a list of pieces and one join at the end.

**Narrator:** You'll walk backward to find the last word. Compare column by column to find a common prefix. Split, reverse, and join to flip word order. Try every start position to find a substring. Use a lookup table for Roman numerals. Simulate a zigzag with a direction flag. And for Text Justification, you'll break a messy job into small helper functions.

*[pause 1s]*

**Narrator:** One more thing before you start. Your mistake log.

**Narrator:** You've logged seven mistakes. This section will test them. Index versus value. Looping over the wrong thing. Calculating without saving. Off by one at the ends. Ignoring the return type. Returning true too early.

**Narrator:** Every lab has a plan block at the top. Write returns, and what it returns, before anything else. That one habit prevents more failures than any trick in this section.

*[pause 1s]*

**Narrator:** That's the map. Seven patterns. Twenty four problems. Open lesson one point one when you're at your desk. Next track goes deeper on the first four patterns.
