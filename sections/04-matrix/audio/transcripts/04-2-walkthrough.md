# 04-2 Matrix Walkthrough

**Narrator:** Section four, track two. The walkthrough. Answer out loud before the answer voice.

*[pause 1s]*

**Narrator:** The grid is one two three, four five six. What is grid one, two?

*[pause 4s]*

**Answer:** Six. Row one is four five six. Column two of it is six.

**Narrator:** How many rows, and how many columns?

*[pause 4s]*

**Answer:** Two rows. Three columns.

*[pause 1s]*

**Narrator:** You build an empty grid by multiplying a row by the number of rows. What goes wrong?

*[pause 5s]*

**Answer:** Every row is the same list. Change one, and they all change. Use a comprehension instead.

*[pause 1s]*

**Narrator:** A cell is in row zero. You look up without a bounds check. What happens?

*[pause 5s]*

**Answer:** Row minus one reads the last row. No error, just a wrong answer.

*[pause 1s]*

**Narrator:** Transpose a two by three grid. What shape comes out?

*[pause 3s]*

**Answer:** Three by two.

**Narrator:** Where does row r, column c go?

*[pause 3s]*

**Answer:** To row c, column r.

*[pause 1s]*

**Narrator:** An n by n grid. Which cells are on the main diagonal?

*[pause 3s]*

**Answer:** Where the row equals the column.

**Narrator:** And the anti-diagonal?

*[pause 4s]*

**Answer:** Where row plus column equals n minus one.

**Narrator:** When n is odd, what do you watch for?

*[pause 4s]*

**Answer:** The center cell is on both diagonals. Count it once.

*[pause 1s]*

**Narrator:** Valid Sudoku. Which box is cell four, seven in?

*[pause 6s]*

**Answer:** Box five. Four divided by three is one. One times three is three. Seven divided by three is two. Three plus two is five.

**Narrator:** When can you return true?

*[pause 3s]*

**Answer:** Only after checking every cell.

*[pause 1s]*

**Narrator:** Rotate Image. Ninety degrees clockwise, in place. The steps?

*[pause 4s]*

**Answer:** Transpose. Then reverse each row.

**Narrator:** During the transpose, which cells do you swap?

*[pause 5s]*

**Answer:** Only the cells above the diagonal, where the column is bigger than the row. Otherwise each pair swaps twice and nothing changes.

**Narrator:** Counterclockwise?

*[pause 4s]*

**Answer:** Transpose, then reverse the order of the rows.

*[pause 1s]*

**Narrator:** Spiral Matrix. Name the four walls.

*[pause 3s]*

**Answer:** Top, bottom, left, right.

**Narrator:** After walking the top row, which wall moves?

*[pause 3s]*

**Answer:** Top moves down by one.

**Narrator:** Which steps need a re-check?

*[pause 5s]*

**Answer:** The bottom row and the left column. After two walls move, there might be nothing left.

**Narrator:** Which test cases catch it?

*[pause 4s]*

**Answer:** A single row. And a single column.

*[pause 1s]*

**Narrator:** Set Matrix Zeroes. Why not zero a row and column the moment you see a zero?

*[pause 5s]*

**Answer:** The new zeros would trigger more zeroing. Record first, then write.

**Narrator:** Where does the O of one version keep its record?

*[pause 4s]*

**Answer:** In the first row and first column of the grid.

**Narrator:** Why zero row zero and column zero last?

*[pause 4s]*

**Answer:** They hold the flags the other cells still need.

*[pause 1s]*

**Narrator:** Game of Life. A cell holds a two. What does it mean?

*[pause 4s]*

**Answer:** It was live, and it will be dead.

**Narrator:** And a three?

*[pause 3s]*

**Answer:** It was dead, and it will be live.

**Narrator:** Which values count as live neighbors during the first pass?

*[pause 4s]*

**Answer:** One and two. The cells that were live before.

*[pause 1s]*

**Narrator:** Last one. A new problem. Is this grid the same after a half turn? What do you compare?

*[pause 6s]*

**Answer:** Each cell r, c against cell m minus one minus r, n minus one minus c. No copy needed.

*[pause 1s]*

**Narrator:** That's the walkthrough. Next track is the rapid fire drill.
