# All Pattern Triggers

One table for the whole course. It grows by a few rows each section. Read the whole thing every week: it takes
five minutes, and it's the best interleaving drill in the course. Cover the right two columns and name the
pattern from the trigger alone.

| Trigger in the problem | Pattern | Core move | Section |
|---|---|---|---|
| "have I seen this before?" | set | `if x in seen` | 00 |
| frequency, count, anagram | Counter / dict | `counts[x] = counts.get(x, 0) + 1` | 00 |
| need a partner value | dict value → index | look up `target - x`, then store x | 00 |
| group things by a key | `defaultdict(list)` | `groups[key].append(x)` | 00 |
| remove from the front repeatedly | deque | `popleft()` | 00 |
| running total, totals up to i | prefix sum | answer[i] = answer[i-1] + x | 00 |
| in place, return k, first k elements | read/write pointers | copy keepers to `write` | 01 |
| merge into a list with space at the end | fill from the back | three pointers, biggest last | 01 |
| appears more than n/2 times | Boyer–Moore voting | candidate + count | 01 |
| "at least h items with at least h" | sort + compare to position | value ≥ 1-based position | 01 |
| rotate, circular, wrap around | modulo / reversals | `(i + k) % n`; reverse all, first k, rest | 01 |
| best pair, one before the other | best-so-far scan | track min so far | 01 |
| unlimited transactions | greedy sum of rises | add every positive daily change | 01 |
| can you reach the end? | farthest reach | stuck if `i > reach` | 01 |
| fewest jumps over ranges | rings (BFS levels) | jumps, ring_end, farthest | 01 |
| circular route, find the start | total check + reset | start = i + 1 when tank < 0 | 01 |
| for each i, everything else | prefix + suffix passes | sweep both ways, combine | 01 |
| limited by the shorter side | min of two maxes | `min(max_left, max_right) - h[i]` | 01 |
| two neighbor rules | one sweep per side | merge with `max` | 01 |
| O(1) insert, delete, and random | list + dict | swap with last, pop | 01 |
| common prefix | column by column | stop at mismatch or short word | 01 |
| symbol ↔ value | lookup table | peek next; greedy biggest-first | 01 |
| odd layout (zigzag, spiral) | simulate | direction flag | 01 |
| sorted list + find a pair | opposite ends | too small → left, too big → right | 02 |
| reads the same both ways | opposite ends | compare outside pair, step inward | 02 |
| sorted with negatives, output by size | ends hold the biggest magnitudes | fill the output from the back | 02 |
| "in order, gaps allowed" across two sequences | same direction | slow pointer moves only on a match | 02 |
| maximize, capped by the shorter side | shrink the weaker side | move the shorter line | 02 |
| k numbers that sum to X | sort + fix + two pointers | skip equal neighbors | 02 |
| prefix/suffix answer, but O(1) space | two pointers from the ends | process the side whose bound is known | 02 |
