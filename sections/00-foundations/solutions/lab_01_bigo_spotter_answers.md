# Lab 0.01 — Big-O Spotter: Answers

| Q | Answer | Why |
|---|---|---|
| b1 | O(n) | Inner loop is always 10. Constants drop. |
| b2 | O(log n) | `i` doubles each pass. |
| b3 | O(n log n) | Sort is n log n; the loop after is n; the bigger term wins. |
| b4 | O(n^2) | `in` on a **list** is a hidden O(n) loop, inside an O(n) loop. |
| b5 | O(n) | Building the set is O(n). Each `in` on a set is O(1). |
| b6 | O(n^2) | About n²/2 pairs. The /2 drops. |
| b7 | O(1) | Dict lookup by key. |
| b8 | O(n) | Two loops in a row: n + n = 2n. |
| b9 | O(n^2) | `pop(0)` shifts the whole list each time. Use `deque.popleft()` for O(n). |
| b10 | O(n) | Append is O(1). One join at the end is linear. |
| b11 | O(n^3) | Three nested loops over n. |
| b12 | O(log n) | Binary search halves the range each pass. |
| s1 | O(n) | The set can grow to hold every item. |
| s2 | O(1) | Two index variables. The swaps happen inside the input. |
