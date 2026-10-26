"""Images for the Section 00 deck. Run automatically by tools/build_anki.py."""
from card_images import array_diagram, before_after, bigo_chart, code_image, table_image


def build(out):
    bigo_chart(out / "bigo_ladder.png", n_max=20)
    bigo_chart(out / "bigo_n_log_n.png", n_max=20, mark="n log n")
    bigo_chart(out / "bigo_log_n.png", show=("1", "log n", "n"), n_max=64, mark="log n")
    bigo_chart(out / "bigo_linear.png", show=("1", "log n", "n", "n^2"), n_max=20, mark="n")

    code_image("for x in nums:      # n steps\n    ...\nfor y in nums:      # + n steps\n    ...\n# total: 2n  ->  O(n)",
               out / "code_loops_in_a_row.png")
    code_image("for x in nums:          # n times...\n    for y in nums:      # ...n steps EACH time\n        ...\n# total: n * n  ->  O(n^2)",
               out / "code_nested_loops.png")
    code_image("while n > 1:\n    n = n // 2\n# n = 16 -> 8 -> 4 -> 2 -> 1\n# 4 passes. log2(16) = 4",
               out / "code_halving.png")
    code_image("for x in nums:          # n times...\n    if x + 1 in nums:   # ...hidden scan of n\n        ...\n# real cost: O(n^2)\n\nseen = set(nums)        # fix: build once, O(n)\nfor x in nums:\n    if x + 1 in seen:   # O(1) lookup\n        ...",
               out / "code_hidden_in.png")
    code_image("for i in range(n):\n    window = nums[i:i + k]   # copies k items every pass\n# O(n * k)", out / "code_slice_loop.png")
    code_image("for i in range(n):\n    total = sum(nums[:i])    # O(i) each pass\n# O(n^2). Keep a running total instead.",
               out / "code_sum_in_loop.png")

    rows = [
        ["O(log n)", "17", "instant"],
        ["O(n)", "100,000", "instant"],
        ["O(n log n)", "1.7 million", "~0.1 s"],
        ["O(n²)", "10 billion", "~8 minutes"],
        ["O(2ⁿ)", "never", "never"],
    ]
    table_image(["Big-O", "steps at n = 100,000", "Python time"], rows, out / "table_n_1e5.png",
                highlight_rows=(1, 2), col_widths=[1.3, 1.9, 1.4])
    rows_k = [
        ["O(n)", "1,000", "instant"],
        ["O(n²)", "1 million", "~0.05 s"],
        ["O(n³)", "1 billion", "~1 minute"],
    ]
    table_image(["Big-O", "steps at n = 1,000", "Python time"], rows_k, out / "table_n_1e3.png",
                highlight_rows=(1,), col_widths=[1.3, 1.9, 1.4])
    rows_s = [["O(2ⁿ)", "~1 million", "~0.05 s"], ["O(n!)", "2.4 × 10¹⁸", "never"]]
    table_image(["Big-O", "steps at n = 20", "Python time"], rows_s, out / "table_n_20.png",
                highlight_rows=(0,), col_widths=[1.3, 1.9, 1.4])

    array_diagram([7, 3, 9, 4, 1], out / "arr_list_scan.png", pointers={"checks each": 0},
                  highlight=(0, 1, 2, 3, 4), title="x in my_list: looks at every box until it finds x")
    before_after([7, 3, 9, 4, 1], [3, 9, 4, 1], out / "arr_pop0.png",
                 before_title="before pop(0): remove the 7 at index 0",
                 after_title="after: 3, 9, 4, 1 each moved one slot left (n moves)",
                 after_kw={"highlight": (0, 1, 2, 3)})
    before_after([7, 3, 9, 4, 1], [7, 3, 9, 4], out / "arr_pop_end.png",
                 before_title="before pop(): remove the 1 at the end",
                 after_title="after: nothing else moved (1 step)")
