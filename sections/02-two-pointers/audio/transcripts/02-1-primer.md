# 02-1 Two Pointers Primer

**Narrator:** Section two, track one. Two pointers. The primer.

**Narrator:** Listen before you open lesson two point one. You're loading the words, not memorizing.

*[pause 1s]*

**Narrator:** Two pointers means two index variables walking through the data at the same time. Instead of a loop inside a loop, you get one pass. O of n squared becomes O of n.

**Narrator:** You've already used it. In section zero you reversed a list with one pointer at each end. In section one, read and write pointers removed items in place. This section makes the idea deliberate.

*[pause 1s]*

**Narrator:** There are four shapes.

**Narrator:** Shape one. Opposite ends. One pointer starts at the left, one at the right. They walk toward each other.

**Narrator:** Use it for symmetry. A palindrome reads the same both ways, so you compare the outside pair, then step inward.

**Narrator:** And use it for pairs in a sorted list. Two Sum two. The list is sorted. You want two numbers that add to a target. Start with the smallest and the biggest. If the sum is too small, move the left pointer, to bring in a bigger number. If it's too big, move the right pointer, to bring in a smaller one.

**Narrator:** Here's the sentence that makes it work. When the sum is too small, the right pointer holds the biggest partner still available. If even that isn't enough, the left number has no partner at all. You can throw it away.

**Narrator:** Every two pointer problem has a sentence like that. Why is it safe to move this pointer? Learn to say it. Interviewers ask it constantly.

*[pause 1s]*

**Narrator:** Shape two. Same direction. Both pointers move forward, at different speeds.

**Narrator:** Is Subsequence asks: can you find the letters of one string inside another, in order, with gaps allowed? One pointer per string. The pointer in the long string moves every step. The pointer in the short string moves only when the letters match.

*[pause 1s]*

**Narrator:** Shape three. Shrink the weaker side.

**Narrator:** Container With Most Water. Vertical lines. Pick two. The water they hold is the width between them, times the shorter line.

**Narrator:** Start at both ends, the widest container. Then move the shorter line inward. Why? Any container that keeps the shorter line is narrower and no taller. It can't win. So the shorter line is finished.

*[pause 1s]*

**Narrator:** Shape four. Sort first, then two pointers.

**Narrator:** Three Sum asks for every triple that adds to zero, with no repeats. Sort the list. Fix the first number. Now you need two numbers that add to minus that number. That's Two Sum two, which you just learned. Run it on the rest of the list.

**Narrator:** Sorting also lines up duplicates side by side. So skipping repeats becomes easy. You'll skip in three places.

*[pause 1s]*

**Narrator:** And one return visit. Trapping Rain Water, from section one. Last time you used two extra lists. This time, two pointers and a few variables. Same answer. Constant space.

*[pause 1s]*

**Narrator:** One new bug to watch for. Moving the wrong pointer. If the sum is too small and you move the right pointer, the sum gets smaller still. The bug hunt lab has it. If it catches you, it becomes mistake M eight.

*[pause 1s]*

**Narrator:** That's the map. Four shapes. One question that matters most: why is it safe to move that pointer? Open lesson two point one at your desk.
