# 02-2 Two Pointers Walkthrough

**Narrator:** Section two, track two. The walkthrough. Answer out loud before the answer voice.

*[pause 1s]*

**Narrator:** Valid Palindrome. Ignore anything that isn't a letter or digit. Ignore case. Does it read the same both ways?

**Narrator:** What do you compare at each step?

*[pause 3s]*

**Answer:** The character at left and the character at right, both lowercased.

**Narrator:** And when the character at left is a comma?

*[pause 3s]*

**Answer:** Skip it. Move left forward until it's on a letter or digit.

**Narrator:** That skip loop needs a second check. What is it?

*[pause 4s]*

**Answer:** Left is less than right. Otherwise a string of only punctuation runs off the end.

*[pause 1s]*

**Narrator:** Two Sum two. Sorted list. Find the pair that adds to the target. Return positions starting from one.

**Narrator:** Numbers are one, three, four, eight. Target is seven. Start at the ends. One plus eight is nine. What moves?

*[pause 4s]*

**Answer:** Right moves. Nine is too big. Only a smaller right number can bring it down.

**Narrator:** Now one plus four is five. What moves?

*[pause 3s]*

**Answer:** Left moves. Five is too small.

**Narrator:** Three plus four is seven. What do you return?

*[pause 4s]*

**Answer:** Two and three. The positions, counted from one.

**Narrator:** Say the reason it's safe to drop the left number when the sum is too small.

*[pause 6s]*

**Answer:** The right number is the biggest partner left. If even it isn't enough, the left number has no partner.

*[pause 1s]*

**Narrator:** Squares of a Sorted Array. Negative four, negative one, zero, three, ten. Return the squares, sorted.

**Narrator:** Where are the biggest squares?

*[pause 4s]*

**Answer:** At the two ends. The most negative and the most positive.

**Narrator:** So where does each big square go?

*[pause 3s]*

**Answer:** Into the last open slot of the answer. Fill from the back.

*[pause 1s]*

**Narrator:** Is Subsequence. Is a c e inside a b c d e, in order?

**Narrator:** Which pointer moves every step?

*[pause 3s]*

**Answer:** The one in the longer string, t.

**Narrator:** When does the other one move?

*[pause 3s]*

**Answer:** Only on a match.

**Narrator:** When do you return true?

*[pause 3s]*

**Answer:** When the pointer in s reaches the end of s.

*[pause 1s]*

**Narrator:** Container With Most Water. What's the area of two lines?

*[pause 4s]*

**Answer:** The width between them, times the shorter line.

**Narrator:** The left line is three tall. The right line is ten tall. Which one moves?

*[pause 3s]*

**Answer:** The left. The shorter one.

**Narrator:** Why?

*[pause 6s]*

**Answer:** Every container that keeps the short line is narrower and no taller. None can beat the one you just measured.

*[pause 1s]*

**Narrator:** Three Sum. Find every unique triple that sums to zero.

**Narrator:** First step?

*[pause 3s]*

**Answer:** Sort the list.

**Narrator:** Then?

*[pause 5s]*

**Answer:** For each index i, fix that number, and run Two Sum two on the rest, looking for minus that number.

**Narrator:** Big O?

*[pause 3s]*

**Answer:** O of n squared.

**Narrator:** Name the three duplicate skips.

*[pause 8s]*

**Answer:** Skip a fixed number that equals the one before it. After a match, move left past repeats. And move right past repeats.

**Narrator:** For the fixed number, why compare with the one before, and not the one after?

*[pause 6s]*

**Answer:** Comparing with the one after skips the first copy. Then a triple like minus one, minus one, two is lost.

**Narrator:** The fixed number is positive. What now?

*[pause 3s]*

**Answer:** Break. Everything after it is positive too.

*[pause 1s]*

**Narrator:** Three Sum Closest. What changes?

*[pause 5s]*

**Answer:** Track the sum closest to the target. Return right away on an exact hit. No duplicate skipping.

*[pause 1s]*

**Narrator:** Trapping Rain Water with two pointers. Left max is three. Right max is seven. Which side is ready?

*[pause 4s]*

**Answer:** The left side. Its level is three for sure, because the right already has a taller bar.

**Narrator:** What did this version save over section one's?

*[pause 3s]*

**Answer:** Space. No extra lists. O of one.

*[pause 1s]*

**Narrator:** Last one. A new problem. Sorted list. Count the pairs whose sum is below k. Which shape?

*[pause 5s]*

**Answer:** Opposite ends. When the pair at left and right is below k, every pair from left to anything up to right works. Add right minus left, then move left.

*[pause 1s]*

**Narrator:** That's the walkthrough. Next track is the rapid fire drill.
