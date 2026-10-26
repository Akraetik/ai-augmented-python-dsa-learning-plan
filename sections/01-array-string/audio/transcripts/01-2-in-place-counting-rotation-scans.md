# 01-2 In Place, Counting, Rotation, Scans

**Narrator:** Section one, track two. In place edits, counting, rotation, and scans. Lessons one point one through one point four.

**Narrator:** Answer the questions out loud before the answer voice does.

*[pause 1s]*

**Narrator:** The read and write pointer pattern has three parts. Say them with me.

**Narrator:** Set write to zero. For each item, if it passes the keep rule, copy it to the write slot and move write forward. Return write.

*[pause 1s]*

**Narrator:** Only the keep rule changes from problem to problem.

**Narrator:** Remove Element. What's the keep rule?

*[pause 3s]*

**Answer:** Keep the item if it's not the value we're removing.

**Narrator:** Remove Duplicates, on a sorted list. What's the keep rule?

*[pause 3s]*

**Answer:** Keep it if write is zero, or if it's different from the last kept item, at write minus one.

**Narrator:** Remove Duplicates two allows each value twice. What's the keep rule?

*[pause 4s]*

**Answer:** Keep it if write is less than two, or if it's different from the item two kept slots back, at write minus two.

**Narrator:** Why compare with the kept region, and not with the items just behind read?

*[pause 4s]*

**Answer:** Because earlier writes may have changed what's behind read. The kept region is the only part you can trust.

*[pause 1s]*

**Narrator:** What do you return from these problems? The list, or a number?

*[pause 3s]*

**Answer:** A number. k, how many items you kept. The list is changed in place.

**Narrator:** Here's a trap. Inside your function, you build a new list and write nums equals new list. What does the caller see?

*[pause 4s]*

**Answer:** Nothing changes. That only renames the local variable. You have to change the contents, by index, or with a slice assignment.

*[pause 1s]*

**Narrator:** Merge Sorted Array. Two sorted lists. The first has empty space at the end. Merge the second into the first.

**Narrator:** Why fill from the back?

*[pause 4s]*

**Answer:** The back is empty. Writing there never destroys a value you haven't read yet.

**Narrator:** You use three positions. The last real item of list one. The last item of list two. And the last slot overall. Each step, the bigger of the two goes into the last slot.

**Narrator:** When list two runs out first, are you done?

*[pause 3s]*

**Answer:** Yes. List one's leftovers are already in place.

**Narrator:** When list one runs out first?

*[pause 3s]*

**Answer:** Copy the rest of list two in.

*[pause 1s]*

**Narrator:** Now counting. Majority Element. One value fills more than half the list.

**Narrator:** Name three ways to find it, with their costs.

*[pause 6s]*

**Answer:** Count with a Counter. Linear time, linear space. Sort and take the middle. N log n. Or Boyer Moore voting. Linear time, constant space.

**Narrator:** Why does the middle of the sorted list always hold the majority?

*[pause 4s]*

**Answer:** The majority covers more than half the slots. Any block that big must cover the middle.

**Narrator:** Walk through Boyer Moore.

*[pause 6s]*

**Answer:** Keep a candidate and a count. If the count is zero, the current item becomes the candidate. If the item matches the candidate, add one. If not, subtract one. The survivor is the answer.

**Narrator:** And the catch?

*[pause 3s]*

**Answer:** It only works because a majority is guaranteed. Without that, you'd need a second pass to check.

*[pause 1s]*

**Narrator:** H Index. A researcher's h index is the biggest h where they have h papers with at least h citations each.

**Narrator:** Sort the citations biggest first. Number the papers from one. Then walk down. While the citations are at least the paper number, h is that paper number.

**Narrator:** In H Index, which is the value and which is the position?

*[pause 4s]*

**Answer:** The value is the citation count. The position, counting from one, is the h you're testing. Mixing them is mistake M one.

*[pause 1s]*

**Narrator:** Rotation. Rotate Array right by k.

**Narrator:** Where does the item at index i go?

*[pause 3s]*

**Answer:** To i plus k, mod n.

**Narrator:** k is ten and the list has seven items. How far do you really rotate?

*[pause 3s]*

**Answer:** Three. Ten mod seven.

**Narrator:** Now the constant space trick. Three reversals. In what order, for a right rotation?

*[pause 5s]*

**Answer:** Reverse the whole list. Then reverse the first k. Then reverse the rest.

**Narrator:** Why does that work?

*[pause 5s]*

**Answer:** Reversing the whole list moves the last k items to the front, but backward. It moves the rest to the back, also backward. Reversing each block fixes its order.

**Narrator:** A rotation that pops from the end and inserts at the front, k times. What's wrong with it?

*[pause 4s]*

**Answer:** Insert at the front is linear time. Doing it k times is n times k. Too slow.

*[pause 1s]*

**Narrator:** Scans. Best Time to Buy and Sell Stock. One trade.

**Narrator:** What two things do you track?

*[pause 3s]*

**Answer:** The lowest price so far. And the best profit so far.

**Narrator:** What does best start at, and why?

*[pause 4s]*

**Answer:** Zero. If prices only fall, the answer is zero. No trade.

**Narrator:** Why not start the lowest price at zero?

*[pause 4s]*

**Answer:** Prices are positive. The lowest would never update. Start at the first price, or at infinity.

**Narrator:** Prices are four, nine, one, six. What's the answer?

*[pause 5s]*

**Answer:** Five. Buy at four, sell at nine. Or buy at one, sell at six. Both give five.

*[pause 1s]*

**Narrator:** Stock two. Trade as often as you like. What's the whole algorithm?

*[pause 4s]*

**Answer:** Add up every positive difference between one day and the day before.

**Narrator:** Why is greedy safe here?

*[pause 5s]*

**Answer:** Any climb equals the sum of its daily steps. Taking one step never blocks another. So the sum of all the gains is the best total.

**Narrator:** Prices one, three, two, five. Answer?

*[pause 4s]*

**Answer:** Five. Two from one to three. Three from two to five.

*[pause 1s]*

**Narrator:** Last one for this track. A new problem. You're given temperatures, in order. Find the biggest drop, where the higher reading comes first. Which pattern?

*[pause 5s]*

**Answer:** A best so far scan. Track the highest reading so far, and the biggest drop from it.

*[pause 1s]*

**Narrator:** That's the first four patterns. Next track: reach, prefix and suffix passes, and design.
