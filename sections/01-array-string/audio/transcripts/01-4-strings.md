# 01-4 Strings

**Narrator:** Section one, track four. Strings. Lesson one point eight.

**Narrator:** Eight problems. Each one trains a different string skill. Let's go through them.

*[pause 1s]*

**Narrator:** First, the ground rules. A string reads like a list. Index it. Slice it. Loop over it. But you can't change it.

**Narrator:** To build a new string, what do you do?

*[pause 3s]*

**Answer:** Collect the pieces in a list. Join them once at the end.

*[pause 1s]*

**Narrator:** Length of Last Word. Return the length of the last word. There may be spaces at the end.

**Narrator:** What's the one line answer?

*[pause 4s]*

**Answer:** Split the string, take the last word, and return its length.

**Narrator:** Now the interviewer says: no split. Walk me through it.

*[pause 6s]*

**Answer:** Start at the last index. Walk backward past the spaces. Then count letters until you hit a space or the start.

**Narrator:** In those while loops, which check comes first: i is at least zero, or the character is a space?

*[pause 4s]*

**Answer:** i is at least zero, first. If i hits minus one, Python stops before reading the character.

**Narrator:** That's called short circuiting. It's how you guard an index.

*[pause 1s]*

**Narrator:** Longest Common Prefix. The longest beginning shared by every word.

**Narrator:** Picture the words stacked as rows. Which way do you read?

*[pause 3s]*

**Answer:** Down the columns. One character position at a time.

**Narrator:** Finish this sentence. One pass of my outer loop equals one what?

*[pause 3s]*

**Answer:** One character position.

**Narrator:** That sentence is the fix for mistake M two. You've hit it on this problem before.

**Narrator:** Two reasons to stop. Name them.

*[pause 4s]*

**Answer:** A word has a different letter in this column. Or a word is too short to have this column at all.

*[pause 1s]*

**Narrator:** Reverse Words in a String. Return the words in reverse order, with single spaces, and nothing extra at the ends.

**Narrator:** The one liner?

*[pause 4s]*

**Answer:** Split, reverse, and join with a single space.

**Narrator:** Why does that already handle every spacing case?

*[pause 4s]*

**Answer:** Split with no arguments splits on any run of spaces and drops the empty pieces.

*[pause 1s]*

**Narrator:** Find the First Occurrence. Where does the needle first appear in the haystack?

**Narrator:** The method. Try each possible start. At each one, compare letters until one differs. If you match the whole needle, return the start.

**Narrator:** Haystack is ten long. Needle is four. What's the last start worth trying?

*[pause 4s]*

**Answer:** Six. Ten minus four.

**Narrator:** So your range goes up to what?

*[pause 4s]*

**Answer:** Range of n minus m, plus one. So it includes six.

**Narrator:** That's mistake M five territory. Write the bound in your plan.

*[pause 1s]*

**Narrator:** Roman to Integer. I is one. V is five. X is ten. L is fifty. C is one hundred. D is five hundred. M is one thousand.

**Narrator:** Usually you add. When do you subtract?

*[pause 4s]*

**Answer:** When the next symbol is bigger than this one. Like I before V, or X before C.

**Narrator:** What about the last symbol?

*[pause 3s]*

**Answer:** It has no next. Always add it. Guard the peek.

**Narrator:** X I V. What number?

*[pause 3s]*

**Answer:** Fourteen.

**Narrator:** M C M X C I V?

*[pause 6s]*

**Answer:** Nineteen ninety four.

*[pause 1s]*

**Narrator:** Integer to Roman. The reverse.

**Narrator:** The method is greedy. Take the biggest piece that fits. Subtract. Repeat.

**Narrator:** Thirteen pieces, biggest first. Try to say them.

*[pause 8s]*

**Answer:** One thousand, M. Nine hundred, C M. Five hundred, D. Four hundred, C D. One hundred, C. Ninety, X C. Fifty, L. Forty, X L. Ten, X. Nine, I X. Five, V. Four, I V. One, I.

**Narrator:** Why does including nine hundred, four hundred, and the other pairs matter?

*[pause 5s]*

**Answer:** Without them, greedy would write four as I I I I. The pairs make the greedy choice correct.

*[pause 1s]*

**Narrator:** Zigzag Conversion. Write the string down and up across a number of rows, then read each row left to right.

**Narrator:** Do you hunt for an index formula?

*[pause 3s]*

**Answer:** No. Simulate it.

**Narrator:** What state do you keep?

*[pause 5s]*

**Answer:** One list per row. The current row. And a step that's plus one going down, or minus one going up.

**Narrator:** When does the step flip?

*[pause 4s]*

**Answer:** At the top row and at the bottom row.

**Narrator:** What's the special case?

*[pause 4s]*

**Answer:** One row. Return the string unchanged. Otherwise the step pushes past the only row.

**Narrator:** A B C D E, two rows. What comes out?

*[pause 5s]*

**Answer:** A C E, then B D. So A C E B D.

*[pause 1s]*

**Narrator:** Text Justification. The hard one. It's hard because of bookkeeping, not cleverness.

**Narrator:** Lay out words into lines of an exact width. Pack as many words as fit. Spread the extra spaces. Left gaps get the extras first. The last line is left justified.

**Narrator:** How do you break it up?

*[pause 6s]*

**Answer:** Three helpers. One picks which words fit on a line. One justifies a full line. One left justifies the last line or a single word line.

**Narrator:** Seven spaces, three gaps. How are they spread?

*[pause 5s]*

**Answer:** Three, two, two. Div mod of seven by three is two with one left over. The first gap gets the extra.

**Narrator:** Write each helper alone. Test each one in a scratch file. That's how you'd do it at work, too.

*[pause 1s]*

**Narrator:** Quick fire. Name the skill.

**Narrator:** Trailing spaces.

*[pause 2s]*

**Answer:** Walk backward, and guard the index.

**Narrator:** A prefix shared by every word.

*[pause 2s]*

**Answer:** Column by column.

**Narrator:** Messy spacing.

*[pause 2s]*

**Answer:** Split with no arguments.

**Narrator:** Symbols to numbers.

*[pause 2s]*

**Answer:** A lookup table, and peek at the next symbol.

**Narrator:** A strange layout.

*[pause 2s]*

**Answer:** Simulate with a direction flag.

**Narrator:** A long messy job.

*[pause 2s]*

**Answer:** Break it into helpers.

*[pause 1s]*

**Narrator:** That's strings. The last track is the rapid fire drill for the whole section. Put it on repeat in the week before your gate.
