# Mistakes Log

Every repeated mistake goes here. If it happens twice, it earns a row and a flashcard.
Before you submit any lab, scan this list against your code.

The first seven come from earlier LeetCode 75 practice (Oct 2026). They're already in the Anki decks
under the `mistake` tag.

## Active mistakes

| ID | Mistake | Looks like | The check | Seen | Last seen |
|---|---|---|---|---|---|
| M1 | **Index vs value.** Using a value as if it were a position. | `for num in nums: nums[num] ...` | Ask: "Is this variable a *position* or a *thing at a position*?" If you need both, use `enumerate`. | 3+ | 2026-10 |
| M2 | **Looping over the wrong thing.** Iterating the outer list when you need positions inside each item. | `for ch in strs:` when you meant each column of each string | Say out loud what one pass of the loop *is*. "One pass = one character position." Then write the loop to match. | 2+ | 2026-10 |
| M3 | **Meaningless check.** A line that runs but tests nothing, written when unsure how to test. | `if s[i]:` to mean "is this a vowel?" | If you can't say in plain English what the condition is true for, stop. Write the English first. | 2+ | 2026-10 |
| M4 | **Calculating but not saving.** | `left + 1` instead of `left += 1` | Every pointer move and counter change must have `=` in it. Scan for bare arithmetic. | 2+ | 2026-10 |
| M5 | **Off-by-one at the ends.** | `range(len(a))` then reading `a[i+1]` | Test your loop on a 1-element and a 2-element input, by hand, before running. | 2+ | 2026-10 |
| M6 | **Not reading the return type.** Returning a list when it wants an int, or returning when it wants in-place. | Function says `-> None` but you `return nums` | Read the signature and the last line of the problem *before* the PLAN. Write "RETURNS: ___" at the top of your plan. | 2+ | 2026-10 |
| M7 | **Returning success too early.** `return True` inside the loop after checking one item. | `for x in a: if ok(x): return True` | "True" answers usually come *after* the loop. "False" answers usually come *inside* it. | 2+ | 2026-10 |

## Candidates (seen in a Bug Hunt, not yet made by you)

| ID | Mistake | Looks like | The check | From |
|---|---|---|---|---|
| M8? | **Moving the wrong pointer.** | sum too small, but `right -= 1` | "Which pointer moves the value the way I need?" | Lab 2.09 |

Promote a candidate to the active table the first time you make it yourself.

## How to add a row

1. Give it the next ID (M8, M9 ...).
2. Write the mistake in one line, plus a real snippet of what you typed.
3. Write the check you'll run to catch it next time.
4. Add a card to the section's `anki/cards.py` with the tag `mistake`, then rebuild the deck.

## Retired mistakes

Move a row here when it hasn't shown up in 3 straight sections.

| ID | Mistake | Retired |
|---|---|---|
| | | |
