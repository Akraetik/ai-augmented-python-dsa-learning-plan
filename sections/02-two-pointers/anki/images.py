"""Images for the Section 02 deck. Run automatically by tools/build_anki.py."""
from card_images import array_diagram, bars_diagram, code_image, stack


def build(out):
    code_image("left, right = 0, len(items) - 1\nwhile left < right:\n    # compare items[left], items[right]\n"
               "    # decide which pointer moves, and WHY that side is done\n    ...", out / "code_opposite_ends.png")
    array_diagram(list("racecar"), out / "arr_palindrome.png", pointers={"left": 0, "right": 6},
                  highlight=(0, 6), title="compare the ends, then both step inward")
    stack([
        dict(values=[1, 3, 4, 8], pointers={"left": 0, "right": 3}, highlight=(0, 3), title="1 + 8 = 9 > 7  → too big: right moves"),
        dict(values=[1, 3, 4, 8], pointers={"left": 0, "right": 2}, highlight=(0, 2), faded=(3,), title="1 + 4 = 5 < 7  → too small: left moves"),
        dict(values=[1, 3, 4, 8], pointers={"left": 1, "right": 2}, highlight=(1, 2), faded=(0, 3), title="3 + 4 = 7  → return [2, 3] (1-indexed)"),
    ], out / "steps_two_sum_ii.png")
    stack([
        dict(values=list("ace"), pointers={"i (slow)": 1}, highlight=(0,), title="s: i moves only on a match"),
        dict(values=list("abcde"), pointers={"j (fast)": 2}, highlight=(0, 2), title="t: j moves every step"),
    ], out / "steps_subsequence.png")
    stack([
        dict(values=[-4, -1, 0, 3, 10], pointers={"left": 0, "right": 4}, title="|−4| vs |10| → 100 goes in the LAST slot"),
        dict(values=["_", "_", "_", "_", 100], highlight=(4,), title="output fills from the back"),
    ], out / "steps_squares.png")
    bars_diagram([1, 8, 6, 2, 5, 4, 8, 3, 7], out / "bars_container.png", pair=(1, 8),
                 title="area = width × SHORTER line")
    bars_diagram([1, 8, 6, 2, 5, 4, 8, 3, 7], out / "bars_container_move.png", pair=(0, 8),
                 pointers={"left": 0, "right": 8}, title="left (1) is shorter → it can never do better → move it")
    array_diagram([-4, -1, -1, 0, 1, 2], out / "arr_three_sum.png", pointers={"i": 1, "left": 2, "right": 5},
                  highlight=(1, 2, 5), title="sorted · fix i · two-pointer the rest for −nums[i]")
    code_image("if i > 0 and nums[i] == nums[i - 1]:\n    continue                 # 1. repeated fixed value\n...\n"
               "out.append([nums[i], nums[left], nums[right]])\nleft += 1; right -= 1\n"
               "while left < right and nums[left] == nums[left - 1]:\n    left += 1                # 2. repeated left value\n"
               "while left < right and nums[right] == nums[right + 1]:\n    right -= 1               # 3. repeated right value",
               out / "code_three_sum_skips.png")
    bars_diagram([2, 0, 3, 1, 4, 2], out / "bars_trap.png", trapped=True, pointers={"left": 1, "right": 4},
                 title="left_max 2 < right_max 4 → water at left is known: 2 − 0 = 2")
    code_image("left_max = max(left_max, h[left])\nright_max = max(right_max, h[right])\nif left_max < right_max:\n"
               "    total += left_max - h[left]     # left's level is known\n    left += 1\nelse:\n"
               "    total += right_max - h[right]\n    right -= 1", out / "code_trap_two_pointers.png")
