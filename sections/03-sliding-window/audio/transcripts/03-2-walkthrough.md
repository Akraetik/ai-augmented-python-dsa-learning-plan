# 03-2 Sliding Window Walkthrough

**Narrator:** Section three, track two. The walkthrough. Answer out loud before the answer voice.

*[pause 1s]*

**Narrator:** Fixed window. Numbers two, one, five, one, three, two. Window size three. The first window sums to eight. Slide one step. What enters, and what leaves?

*[pause 4s]*

**Answer:** One enters. Two leaves. The sum becomes seven.

**Narrator:** Slide again. What's the new sum?

*[pause 4s]*

**Answer:** Three enters, one leaves. Seven plus three minus one is nine.

**Narrator:** In code, when nums at right enters, which index leaves?

*[pause 4s]*

**Answer:** Right minus k.

*[pause 1s]*

**Narrator:** Permutation in String. Does s two contain a rearrangement of s one? What do you compare?

*[pause 4s]*

**Answer:** Letter counts. Slide a window the length of s one, and compare its counts to s one's counts.

*[pause 1s]*

**Narrator:** Now the longest valid template. Say the three steps.

*[pause 5s]*

**Answer:** Grow by adding the right item. Shrink from the left while the window is broken. Record the length after the while loop.

**Narrator:** What's the length of a window from left to right?

*[pause 3s]*

**Answer:** Right minus left plus one.

*[pause 1s]*

**Narrator:** Longest Substring Without Repeating Characters. The string is p w w k e w. The second w arrives. What happens?

*[pause 6s]*

**Answer:** The window p w w is broken. Shrink. Drop p. Still broken. Drop the first w. Now the window is just w. Valid.

**Narrator:** Why does that need a while, not an if?

*[pause 4s]*

**Answer:** One step wasn't enough. It took two drops to fix the window.

**Narrator:** What's the final answer for p w w k e w?

*[pause 3s]*

**Answer:** Three. W k e.

*[pause 1s]*

**Narrator:** Max Consecutive Ones three. You may flip k zeros. Restate it as a window rule.

*[pause 4s]*

**Answer:** The longest window with at most k zeros in it.

*[pause 1s]*

**Narrator:** Longest Repeating Character Replacement. How many changes does a window need?

*[pause 5s]*

**Answer:** The window length, minus the count of its most common letter.

**Narrator:** When is it broken?

*[pause 3s]*

**Answer:** When that number is more than k.

*[pause 1s]*

**Narrator:** Now the shortest valid template. Say the steps.

*[pause 5s]*

**Answer:** Grow by adding the right item. While the window is valid, record its length, then shrink from the left.

**Narrator:** Name the three differences from the longest template.

*[pause 7s]*

**Answer:** The while runs when valid, not when broken. You record inside the while, not after. And best starts at infinity, not zero.

*[pause 1s]*

**Narrator:** Minimum Size Subarray Sum. Target seven. Numbers two, three, one, two, four, three. What's the answer?

*[pause 5s]*

**Answer:** Two. The window four, three.

**Narrator:** Nothing ever reaches the target. What do you return?

*[pause 3s]*

**Answer:** Zero.

**Narrator:** Why must the numbers be positive?

*[pause 5s]*

**Answer:** So growing raises the sum and shrinking lowers it. With negatives, shrinking can raise the sum, and the window can't tell which way to move.

*[pause 1s]*

**Narrator:** Minimum Window Substring. When does have go up?

*[pause 5s]*

**Answer:** When a letter's count in the window reaches exactly what t needs.

**Narrator:** When does it go down?

*[pause 4s]*

**Answer:** When a letter leaves and its count drops below what t needs.

**Narrator:** What do you record?

*[pause 3s]*

**Answer:** The start and the length. You return the substring.

*[pause 1s]*

**Narrator:** Concatenation of All Words. Every word is three letters. How many window runs do you do?

*[pause 4s]*

**Answer:** Three. One for each starting offset, zero, one, and two.

*[pause 1s]*

**Narrator:** Last one. A new problem. Longest subarray with sum at most k, and the numbers can be negative. Sliding window?

*[pause 5s]*

**Answer:** No. Negatives break it. Think prefix sums.

*[pause 1s]*

**Narrator:** That's the walkthrough. Next track is the rapid fire drill.
