"""Images for the Section 03 deck. Run automatically by tools/build_anki.py."""
from card_images import code_image, stack


def build(out):
    nums = [2, 1, 5, 1, 3, 2]
    stack([
        dict(values=nums, highlight=(0, 1, 2), pointers={"left": 0, "right": 2}, title="window [2 1 5] → sum 8"),
        dict(values=nums, highlight=(1, 2, 3), faded=(0,), pointers={"left": 1, "right": 3}, title="1 enters, 2 leaves → 8 + 1 − 2 = 7"),
        dict(values=nums, highlight=(2, 3, 4), faded=(0, 1), pointers={"left": 2, "right": 4}, title="3 enters, 1 leaves → 7 + 3 − 1 = 9"),
    ], out / "steps_fixed_window.png")
    code_image("window = sum(nums[:k])          # first window, once\nbest = window\nfor right in range(k, len(nums)):\n"
               "    window += nums[right]       # enters\n    window -= nums[right - k]   # leaves\n    best = max(best, window)",
               out / "code_fixed_window.png")
    code_image("left = 0; best = 0\nfor right in range(len(s)):\n    # 1. GROW: add s[right]\n    while BROKEN:\n"
               "        # 2. SHRINK: remove s[left]\n        left += 1\n    # 3. RECORD (after the while)\n"
               "    best = max(best, right - left + 1)", out / "code_longest_template.png")
    code_image("left = 0; best = float('inf')\nfor right in range(len(nums)):\n    # 1. GROW: add nums[right]\n"
               "    while VALID:\n        # 2. RECORD (inside the while)\n        best = min(best, right - left + 1)\n"
               "        # 3. SHRINK: remove nums[left]\n        left += 1\nreturn 0 if best == float('inf') else best",
               out / "code_shortest_template.png")
    s = list("abcabcbb")
    stack([
        dict(values=s, highlight=(0, 1, 2), pointers={"left": 0, "right": 2}, title="window 'abc' → best 3"),
        dict(values=s, highlight=(0, 1, 2, 3), pointers={"left": 0, "right": 3}, title="'a' enters → repeat → broken"),
        dict(values=s, highlight=(1, 2, 3), faded=(0,), pointers={"left": 1, "right": 3}, title="shrink: drop the old 'a' → 'bca' valid"),
    ], out / "steps_longest_substring.png")
    stack([
        dict(values=[1, 0, 1, 1, 0, 1], highlight=(0, 1, 2, 3), pointers={"left": 0, "right": 3}, title="k = 1: one zero inside → valid, length 4"),
        dict(values=[1, 0, 1, 1, 0, 1], highlight=(0, 1, 2, 3, 4), pointers={"left": 0, "right": 4}, title="second zero enters → broken"),
        dict(values=[1, 0, 1, 1, 0, 1], highlight=(2, 3, 4), faded=(0, 1), pointers={"left": 2, "right": 4}, title="shrink past the first zero → valid again"),
    ], out / "steps_ones_iii.png")
    nums = [2, 3, 1, 2, 4, 3]
    stack([
        dict(values=nums, highlight=(1, 2, 3, 4), faded=(0,), pointers={"left": 1, "right": 4}, title="sum 10 ≥ 7 → record 4, then shrink"),
        dict(values=nums, highlight=(2, 3, 4), faded=(0, 1), pointers={"left": 2, "right": 4}, title="sum 7 ≥ 7 → record 3, then shrink"),
        dict(values=nums, highlight=(3, 4), faded=(0, 1, 2), pointers={"left": 3, "right": 4}, title="sum 6 < 7 → stop shrinking, grow right"),
    ], out / "steps_min_subarray.png")
    stack([
        dict(values=list("barfoothefoobarman")[:9], highlight=(0, 1, 2, 3, 4, 5), title="offset 0: bar | foo | the ..."),
        dict(values=list("barfoothefoobarman")[:9], highlight=(1, 2, 3, 4, 5, 6), title="offset 1: arf | oot | hef ..."),
        dict(values=list("barfoothefoobarman")[:9], highlight=(2, 3, 4, 5, 6, 7), title="offset 2: rfo | oth | efo ..."),
    ], out / "steps_word_offsets.png")
