# 03-1 Sliding Window Primer

**Narrator:** Section three, track one. Sliding window. The primer.

**Narrator:** Listen before you open lesson three point one. You're loading the words, not memorizing.

*[pause 1s]*

**Narrator:** A window is a run of items sitting next to each other. Index left through index right. A substring is a window. A subarray is a window.

**Narrator:** Many problems ask about every window, or the best window. Checking every window from scratch is slow. The sliding window reuses work. When the window moves one step, only the edges change. The middle stays.

*[pause 1s]*

**Narrator:** There are three templates. Learn all three.

*[pause 1s]*

**Narrator:** Template one. The fixed window. Every window has the same size, k.

**Narrator:** Build the first window once. Then slide. Each slide, one item enters on the right, and one item leaves on the left. Add the one that enters. Remove the one that leaves. That's it.

**Narrator:** Maximum Average Subarray uses this. So does Permutation in String, where the window holds letter counts instead of a sum.

*[pause 1s]*

**Narrator:** Template two. The longest valid window. The size changes.

**Narrator:** The right pointer walks forward one step at a time. Each new item joins the window. If the window now breaks the rule, the left pointer moves forward, dropping items, until the window is valid again. Then record its length.

**Narrator:** Grow. Shrink while broken. Record after.

**Narrator:** Longest Substring Without Repeating Characters is the classic. The rule is: no letter twice. Max Consecutive Ones three is another. The rule is: at most k zeros inside.

*[pause 1s]*

**Narrator:** Template three. The shortest valid window.

**Narrator:** Same two pointers. But now, while the window is valid, you record it first, then shrink, to see if a shorter one still works.

**Narrator:** Grow. While valid, record, then shrink.

**Narrator:** Minimum Size Subarray Sum uses this. So does Minimum Window Substring, one of the best known hard problems.

*[pause 1s]*

**Narrator:** Here's the question interviewers ask. There's a while loop inside a for loop. Isn't that O of n squared?

**Narrator:** No. The left pointer only moves forward. It never goes back. Over the whole run it moves at most n times. The right pointer moves n times. So the total is about two n. O of n.

*[pause 1s]*

**Narrator:** One warning. Sliding windows need the rule to move one way. In Minimum Size Subarray Sum, the numbers are all positive. Growing always raises the sum. Shrinking always lowers it. With negative numbers, that breaks, and the window is the wrong tool. You'll use prefix sums instead, in section five.

*[pause 1s]*

**Narrator:** One new bug to watch for. Shrinking with if instead of while. One step left may not fix the window. Keep shrinking until it's valid. The bug hunt lab has it.

*[pause 1s]*

**Narrator:** That's the map. Three templates. Fixed. Longest valid. Shortest valid. Open lesson three point one at your desk.
