# Review Sheet · 01 Array / String

One page. Seven patterns. If a line looks unfamiliar, open the lesson it names.

## The seven patterns

| # | Pattern | Trigger | Core move | Problems |
|---|---|---|---|---|
| 1.1 | Read/write pointers | in place, return k | copy keepers to `write`, `write += 1` | 88, 27, 26, 80, (283) |
| 1.2 | Counting / voting | > n/2; "h with h" | Counter, Boyer–Moore; sort + compare to position | 169, 274 |
| 1.3 | Index math / reversal | rotate, circular | `(i + k) % n`, `k %= n`; reverse all / first k / rest | 189 |
| 1.4 | Best-so-far scan | best pair, i before j | track min so far + best | 121, 122 |
| 1.5 | Reach / greedy | reach the end, fewest jumps, circular route | `reach`; rings; reset start when tank < 0 | 55, 45, 134 |
| 1.6 | Prefix + suffix | for each i, everything else | sweep → then ← , combine | 238, 42, 135 |
| 1.7 | List + dict design | O(1) insert, delete, random | dict value → index; swap with last, pop | 380 |
| 1.8 | Strings | words, prefixes, symbols, layouts | split/join; columns; lookup table; simulate | 58, 14, 151, 28, 13, 12, 6, 68 |

## Skeletons

```python
# 1.1 read/write
write = 0
for read in range(len(nums)):
    if KEEP(nums[read]):
        nums[write] = nums[read]
        write += 1
return write
```

```python
# 1.4 best-so-far
lowest, best = float("inf"), 0
for x in nums:
    lowest = min(lowest, x)
    best = max(best, x - lowest)
```

```python
# 1.5 reach
reach = 0
for i, step in enumerate(nums):
    if i > reach: return False
    reach = max(reach, i + step)
return True
```

```python
# 1.6 prefix that excludes i: record, THEN include
run = 1
for i in range(n):
    out[i] = run
    run *= nums[i]
```

## Traps to re-check

- Remove Dup II compares with `nums[write - 2]`, not `read - 2`.
- `nums = new_list` doesn't change the caller's list. Use `nums[:] =` or edit by index.
- Rotate: `k %= n` first.
- Jump Game: made it when `reach >= len(nums) - 1`. Jump Game II loops to `len - 1`.
- Product Except Self: start at 1. No division (zeros).
- Candy: second sweep uses `max`.
- RandomizedSet: update the moved element's index.
- Substring starts: `range(n - m + 1)`. Roman: guard the peek on the last symbol. Zigzag: 1 row → return s.

## Interleave check

Name the pattern in five seconds:
1. "Shift a circular list left by k" → ?
2. "For each i, the max to its right" → ?
3. "Return k after removing negatives in place" → ?

<details><summary>Answers</summary>1.3 modulo/reversal · 1.6 suffix pass · 1.1 read/write</details>
