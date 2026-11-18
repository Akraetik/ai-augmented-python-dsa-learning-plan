"""The LeetCode Top Interview 150, with the lesson that unlocks each problem.

One source of truth for:
  * the "LeetCode 150 you can now solve" block at the end of every lesson
  * the unlock table in each section README
  * sections/24-leetcode-150-checklist/

Rebuild everything with:  python tools/build_unlocks.py

Field guide
-----------
PROBLEMS rows: (number, title, slug, difficulty, home_section)
    home_section is the Top 150 category's section number ("01".."23").

LABS: number -> list of (lesson_id, lab path from the repo root)
    A problem with a lab is unlocked by its first lab's lesson.

EARLY: number -> (lesson_id, nudge)
    Problems from a LATER section that you can already solve with what a lesson taught.
    You solve these on LeetCode. The full lab, hints, and solution come in the home section.
    When the home section is built, add the lab to LABS too and KEEP the EARLY entry:
    the stamp stays where you first unlocked it, and the new lab shows up as a "Revisit".

Everything else is unlocked by its home section ("05", "06", ...).
When a new section is built, add its labs to LABS and re-run the builder.
"""

SECTION_NAMES = {
    "00": "Foundations", "01": "Array / String", "02": "Two Pointers", "03": "Sliding Window",
    "04": "Matrix", "05": "Hashmap", "06": "Intervals", "07": "Stack", "08": "Linked List",
    "09": "Binary Tree General", "10": "Binary Tree BFS", "11": "Binary Search Tree",
    "12": "Graph General", "13": "Graph BFS", "14": "Trie", "15": "Backtracking",
    "16": "Divide & Conquer", "17": "Kadane's Algorithm", "18": "Binary Search", "19": "Heap",
    "20": "Bit Manipulation", "21": "Math", "22": "1D DP", "23": "Multidimensional DP",
}

# Sections that exist as folders. Lessons in these get unlock blocks.
SECTION_DIRS = {
    "00": "00-foundations", "01": "01-array-string", "02": "02-two-pointers",
    "03": "03-sliding-window", "04": "04-matrix",
}

PROBLEMS = [
    # 01 Array / String (24)
    (88, "Merge Sorted Array", "merge-sorted-array", "E", "01"),
    (27, "Remove Element", "remove-element", "E", "01"),
    (26, "Remove Duplicates from Sorted Array", "remove-duplicates-from-sorted-array", "E", "01"),
    (80, "Remove Duplicates from Sorted Array II", "remove-duplicates-from-sorted-array-ii", "M", "01"),
    (169, "Majority Element", "majority-element", "E", "01"),
    (189, "Rotate Array", "rotate-array", "M", "01"),
    (121, "Best Time to Buy and Sell Stock", "best-time-to-buy-and-sell-stock", "E", "01"),
    (122, "Best Time to Buy and Sell Stock II", "best-time-to-buy-and-sell-stock-ii", "M", "01"),
    (55, "Jump Game", "jump-game", "M", "01"),
    (45, "Jump Game II", "jump-game-ii", "M", "01"),
    (274, "H-Index", "h-index", "M", "01"),
    (380, "Insert Delete GetRandom O(1)", "insert-delete-getrandom-o1", "M", "01"),
    (238, "Product of Array Except Self", "product-of-array-except-self", "M", "01"),
    (134, "Gas Station", "gas-station", "M", "01"),
    (135, "Candy", "candy", "H", "01"),
    (42, "Trapping Rain Water", "trapping-rain-water", "H", "01"),
    (13, "Roman to Integer", "roman-to-integer", "E", "01"),
    (12, "Integer to Roman", "integer-to-roman", "M", "01"),
    (58, "Length of Last Word", "length-of-last-word", "E", "01"),
    (14, "Longest Common Prefix", "longest-common-prefix", "E", "01"),
    (151, "Reverse Words in a String", "reverse-words-in-a-string", "M", "01"),
    (6, "Zigzag Conversion", "zigzag-conversion", "M", "01"),
    (28, "Find the Index of the First Occurrence in a String",
     "find-the-index-of-the-first-occurrence-in-a-string", "E", "01"),
    (68, "Text Justification", "text-justification", "H", "01"),
    # 02 Two Pointers (5)
    (125, "Valid Palindrome", "valid-palindrome", "E", "02"),
    (392, "Is Subsequence", "is-subsequence", "E", "02"),
    (167, "Two Sum II - Input Array Is Sorted", "two-sum-ii-input-array-is-sorted", "M", "02"),
    (11, "Container With Most Water", "container-with-most-water", "M", "02"),
    (15, "3Sum", "3sum", "M", "02"),
    # 03 Sliding Window (4)
    (209, "Minimum Size Subarray Sum", "minimum-size-subarray-sum", "M", "03"),
    (3, "Longest Substring Without Repeating Characters",
     "longest-substring-without-repeating-characters", "M", "03"),
    (30, "Substring with Concatenation of All Words", "substring-with-concatenation-of-all-words", "H", "03"),
    (76, "Minimum Window Substring", "minimum-window-substring", "H", "03"),
    # 04 Matrix (5)
    (36, "Valid Sudoku", "valid-sudoku", "M", "04"),
    (54, "Spiral Matrix", "spiral-matrix", "M", "04"),
    (48, "Rotate Image", "rotate-image", "M", "04"),
    (73, "Set Matrix Zeroes", "set-matrix-zeroes", "M", "04"),
    (289, "Game of Life", "game-of-life", "M", "04"),
    # 05 Hashmap (9)
    (383, "Ransom Note", "ransom-note", "E", "05"),
    (205, "Isomorphic Strings", "isomorphic-strings", "E", "05"),
    (290, "Word Pattern", "word-pattern", "E", "05"),
    (242, "Valid Anagram", "valid-anagram", "E", "05"),
    (49, "Group Anagrams", "group-anagrams", "M", "05"),
    (1, "Two Sum", "two-sum", "E", "05"),
    (202, "Happy Number", "happy-number", "E", "05"),
    (219, "Contains Duplicate II", "contains-duplicate-ii", "E", "05"),
    (128, "Longest Consecutive Sequence", "longest-consecutive-sequence", "M", "05"),
    # 06 Intervals (4)
    (228, "Summary Ranges", "summary-ranges", "E", "06"),
    (56, "Merge Intervals", "merge-intervals", "M", "06"),
    (57, "Insert Interval", "insert-interval", "M", "06"),
    (452, "Minimum Number of Arrows to Burst Balloons", "minimum-number-of-arrows-to-burst-balloons", "M", "06"),
    # 07 Stack (5)
    (20, "Valid Parentheses", "valid-parentheses", "E", "07"),
    (71, "Simplify Path", "simplify-path", "M", "07"),
    (155, "Min Stack", "min-stack", "M", "07"),
    (150, "Evaluate Reverse Polish Notation", "evaluate-reverse-polish-notation", "M", "07"),
    (224, "Basic Calculator", "basic-calculator", "H", "07"),
    # 08 Linked List (11)
    (141, "Linked List Cycle", "linked-list-cycle", "E", "08"),
    (2, "Add Two Numbers", "add-two-numbers", "M", "08"),
    (21, "Merge Two Sorted Lists", "merge-two-sorted-lists", "E", "08"),
    (138, "Copy List with Random Pointer", "copy-list-with-random-pointer", "M", "08"),
    (92, "Reverse Linked List II", "reverse-linked-list-ii", "M", "08"),
    (25, "Reverse Nodes in k-Group", "reverse-nodes-in-k-group", "H", "08"),
    (19, "Remove Nth Node From End of List", "remove-nth-node-from-end-of-list", "M", "08"),
    (82, "Remove Duplicates from Sorted List II", "remove-duplicates-from-sorted-list-ii", "M", "08"),
    (61, "Rotate List", "rotate-list", "M", "08"),
    (86, "Partition List", "partition-list", "M", "08"),
    (146, "LRU Cache", "lru-cache", "M", "08"),
    # 09 Binary Tree General (14)
    (104, "Maximum Depth of Binary Tree", "maximum-depth-of-binary-tree", "E", "09"),
    (100, "Same Tree", "same-tree", "E", "09"),
    (226, "Invert Binary Tree", "invert-binary-tree", "E", "09"),
    (101, "Symmetric Tree", "symmetric-tree", "E", "09"),
    (105, "Construct Binary Tree from Preorder and Inorder Traversal",
     "construct-binary-tree-from-preorder-and-inorder-traversal", "M", "09"),
    (106, "Construct Binary Tree from Inorder and Postorder Traversal",
     "construct-binary-tree-from-inorder-and-postorder-traversal", "M", "09"),
    (117, "Populating Next Right Pointers in Each Node II",
     "populating-next-right-pointers-in-each-node-ii", "M", "09"),
    (114, "Flatten Binary Tree to Linked List", "flatten-binary-tree-to-linked-list", "M", "09"),
    (112, "Path Sum", "path-sum", "E", "09"),
    (129, "Sum Root to Leaf Numbers", "sum-root-to-leaf-numbers", "M", "09"),
    (124, "Binary Tree Maximum Path Sum", "binary-tree-maximum-path-sum", "H", "09"),
    (173, "Binary Search Tree Iterator", "binary-search-tree-iterator", "M", "09"),
    (222, "Count Complete Tree Nodes", "count-complete-tree-nodes", "E", "09"),
    (236, "Lowest Common Ancestor of a Binary Tree", "lowest-common-ancestor-of-a-binary-tree", "M", "09"),
    # 10 Binary Tree BFS (4)
    (199, "Binary Tree Right Side View", "binary-tree-right-side-view", "M", "10"),
    (637, "Average of Levels in Binary Tree", "average-of-levels-in-binary-tree", "E", "10"),
    (102, "Binary Tree Level Order Traversal", "binary-tree-level-order-traversal", "M", "10"),
    (103, "Binary Tree Zigzag Level Order Traversal", "binary-tree-zigzag-level-order-traversal", "M", "10"),
    # 11 Binary Search Tree (3)
    (530, "Minimum Absolute Difference in BST", "minimum-absolute-difference-in-bst", "E", "11"),
    (230, "Kth Smallest Element in a BST", "kth-smallest-element-in-a-bst", "M", "11"),
    (98, "Validate Binary Search Tree", "validate-binary-search-tree", "M", "11"),
    # 12 Graph General (6)
    (200, "Number of Islands", "number-of-islands", "M", "12"),
    (130, "Surrounded Regions", "surrounded-regions", "M", "12"),
    (133, "Clone Graph", "clone-graph", "M", "12"),
    (399, "Evaluate Division", "evaluate-division", "M", "12"),
    (207, "Course Schedule", "course-schedule", "M", "12"),
    (210, "Course Schedule II", "course-schedule-ii", "M", "12"),
    # 13 Graph BFS (3)
    (909, "Snakes and Ladders", "snakes-and-ladders", "M", "13"),
    (433, "Minimum Genetic Mutation", "minimum-genetic-mutation", "M", "13"),
    (127, "Word Ladder", "word-ladder", "H", "13"),
    # 14 Trie (3)
    (208, "Implement Trie (Prefix Tree)", "implement-trie-prefix-tree", "M", "14"),
    (211, "Design Add and Search Words Data Structure", "design-add-and-search-words-data-structure", "M", "14"),
    (212, "Word Search II", "word-search-ii", "H", "14"),
    # 15 Backtracking (7)
    (17, "Letter Combinations of a Phone Number", "letter-combinations-of-a-phone-number", "M", "15"),
    (77, "Combinations", "combinations", "M", "15"),
    (46, "Permutations", "permutations", "M", "15"),
    (39, "Combination Sum", "combination-sum", "M", "15"),
    (52, "N-Queens II", "n-queens-ii", "H", "15"),
    (22, "Generate Parentheses", "generate-parentheses", "M", "15"),
    (79, "Word Search", "word-search", "M", "15"),
    # 16 Divide & Conquer (4)
    (108, "Convert Sorted Array to Binary Search Tree", "convert-sorted-array-to-binary-search-tree", "E", "16"),
    (148, "Sort List", "sort-list", "M", "16"),
    (427, "Construct Quad Tree", "construct-quad-tree", "M", "16"),
    (23, "Merge k Sorted Lists", "merge-k-sorted-lists", "H", "16"),
    # 17 Kadane's Algorithm (2)
    (53, "Maximum Subarray", "maximum-subarray", "M", "17"),
    (918, "Maximum Sum Circular Subarray", "maximum-sum-circular-subarray", "M", "17"),
    # 18 Binary Search (7)
    (35, "Search Insert Position", "search-insert-position", "E", "18"),
    (74, "Search a 2D Matrix", "search-a-2d-matrix", "M", "18"),
    (162, "Find Peak Element", "find-peak-element", "M", "18"),
    (33, "Search in Rotated Sorted Array", "search-in-rotated-sorted-array", "M", "18"),
    (34, "Find First and Last Position of Element in Sorted Array",
     "find-first-and-last-position-of-element-in-sorted-array", "M", "18"),
    (153, "Find Minimum in Rotated Sorted Array", "find-minimum-in-rotated-sorted-array", "M", "18"),
    (4, "Median of Two Sorted Arrays", "median-of-two-sorted-arrays", "H", "18"),
    # 19 Heap (4)
    (215, "Kth Largest Element in an Array", "kth-largest-element-in-an-array", "M", "19"),
    (502, "IPO", "ipo", "H", "19"),
    (373, "Find K Pairs with Smallest Sums", "find-k-pairs-with-smallest-sums", "M", "19"),
    (295, "Find Median from Data Stream", "find-median-from-data-stream", "H", "19"),
    # 20 Bit Manipulation (6)
    (67, "Add Binary", "add-binary", "E", "20"),
    (190, "Reverse Bits", "reverse-bits", "E", "20"),
    (191, "Number of 1 Bits", "number-of-1-bits", "E", "20"),
    (136, "Single Number", "single-number", "E", "20"),
    (137, "Single Number II", "single-number-ii", "M", "20"),
    (201, "Bitwise AND of Numbers Range", "bitwise-and-of-numbers-range", "M", "20"),
    # 21 Math (6)
    (9, "Palindrome Number", "palindrome-number", "E", "21"),
    (66, "Plus One", "plus-one", "E", "21"),
    (172, "Factorial Trailing Zeroes", "factorial-trailing-zeroes", "M", "21"),
    (69, "Sqrt(x)", "sqrtx", "E", "21"),
    (50, "Pow(x, n)", "powx-n", "M", "21"),
    (149, "Max Points on a Line", "max-points-on-a-line", "H", "21"),
    # 22 1D DP (5)
    (70, "Climbing Stairs", "climbing-stairs", "E", "22"),
    (198, "House Robber", "house-robber", "M", "22"),
    (139, "Word Break", "word-break", "M", "22"),
    (322, "Coin Change", "coin-change", "M", "22"),
    (300, "Longest Increasing Subsequence", "longest-increasing-subsequence", "M", "22"),
    # 23 Multidimensional DP (9)
    (120, "Triangle", "triangle", "M", "23"),
    (64, "Minimum Path Sum", "minimum-path-sum", "M", "23"),
    (63, "Unique Paths II", "unique-paths-ii", "M", "23"),
    (5, "Longest Palindromic Substring", "longest-palindromic-substring", "M", "23"),
    (97, "Interleaving String", "interleaving-string", "M", "23"),
    (72, "Edit Distance", "edit-distance", "M", "23"),
    (123, "Best Time to Buy and Sell Stock III", "best-time-to-buy-and-sell-stock-iii", "H", "23"),
    (188, "Best Time to Buy and Sell Stock IV", "best-time-to-buy-and-sell-stock-iv", "H", "23"),
    (221, "Maximal Square", "maximal-square", "M", "23"),
]

_A = "sections/01-array-string/labs/"
_T = "sections/02-two-pointers/labs/"
_W = "sections/03-sliding-window/labs/"
_M = "sections/04-matrix/labs/"
_F = "sections/00-foundations/labs/"

LABS = {
    # 00 Foundations: two Hashmap problems arrive early as labs
    242: [("00.4", _F + "lab_08_valid_anagram.py")],
    1: [("00.4", _F + "lab_09_two_sum.py")],
    # 01 Array / String
    88: [("1.1", _A + "lab_01_merge_sorted_array.py")],
    27: [("1.1", _A + "lab_02_remove_element.py")],
    26: [("1.1", _A + "lab_03_remove_duplicates.py")],
    80: [("1.1", _A + "lab_04_remove_duplicates_ii.py")],
    169: [("1.2", _A + "lab_05_majority_element.py")],
    274: [("1.2", _A + "lab_06_h_index.py")],
    189: [("1.3", _A + "lab_07_rotate_array.py")],
    121: [("1.4", _A + "lab_08_best_time_stock.py")],
    122: [("1.4", _A + "lab_09_best_time_stock_ii.py")],
    55: [("1.5", _A + "lab_10_jump_game.py")],
    45: [("1.5", _A + "lab_11_jump_game_ii.py")],
    134: [("1.5", _A + "lab_12_gas_station.py")],
    238: [("1.6", _A + "lab_13_product_except_self.py")],
    42: [("1.6", _A + "lab_14_trapping_rain_water.py"),
         ("2.5", _T + "lab_07_trapping_rain_water_ii.py")],
    135: [("1.6", _A + "lab_15_candy.py")],
    380: [("1.7", _A + "lab_16_randomized_set.py")],
    58: [("1.8", _A + "lab_17_length_of_last_word.py")],
    14: [("1.8", _A + "lab_18_longest_common_prefix.py")],
    151: [("1.8", _A + "lab_19_reverse_words.py")],
    28: [("1.8", _A + "lab_20_find_first_occurrence.py")],
    13: [("1.8", _A + "lab_21_roman_to_integer.py")],
    12: [("1.8", _A + "lab_22_integer_to_roman.py")],
    6: [("1.8", _A + "lab_23_zigzag_conversion.py")],
    68: [("1.8", _A + "lab_24_text_justification.py")],
    # 02 Two Pointers
    125: [("2.1", _T + "lab_01_valid_palindrome.py")],
    167: [("2.1", _T + "lab_03_two_sum_ii.py")],
    392: [("2.2", _T + "lab_02_is_subsequence.py")],
    11: [("2.3", _T + "lab_05_container_most_water.py")],
    15: [("2.4", _T + "lab_06_three_sum.py")],
    # 03 Sliding Window
    3: [("3.2", _W + "lab_03_longest_substring.py")],
    209: [("3.3", _W + "lab_06_min_size_subarray_sum.py")],
    76: [("3.3", _W + "lab_07_min_window_substring.py")],
    30: [("3.4", _W + "lab_08_substring_concatenation.py")],
    # 04 Matrix
    36: [("4.2", _M + "lab_03_valid_sudoku.py")],
    48: [("4.3", _M + "lab_04_rotate_image.py")],
    54: [("4.3", _M + "lab_05_spiral_matrix.py")],
    73: [("4.4", _M + "lab_07_set_matrix_zeroes.py")],
    289: [("4.4", _M + "lab_08_game_of_life.py")],
}

EARLY = {
    9: ("00.4", "Compare str(x) to its reverse with [::-1]. Negative numbers are never palindromes. "
                "Later, redo it with only math: build the reversed number digit by digit with % 10 and // 10."),
    383: ("00.4", "Counter(magazine) must have at least as many of every letter as Counter(ransomNote)."),
    205: ("00.4", "Two dicts, one for each direction (s to t and t to s). Any clash in either one means False."),
    290: ("00.4", "Isomorphic Strings with words: split s first. Different lengths means False. "
                  "Then two dicts, one each way."),
    202: ("00.4", "Keep a set of numbers you have seen. Reach 1: True. See a repeat: it loops forever, so False."),
    49: ("00.4", "Key = ''.join(sorted(word)). Collect words under their key in a defaultdict(list). "
                 "Return the dict's values."),
    128: ("00.4", "Put every number in a set. Only start counting at n when n - 1 is NOT in the set. "
                  "That keeps it O(n)."),
    66: ("1.3", "Walk from the last index to the first. A 9 becomes 0 and carries. Anything else: add 1 and return. "
                "Carry off the front: put a 1 at index 0."),
    67: ("1.3", "One index at the right end of each string, plus a carry. Add digit by digit, collect the "
                "results, then reverse and join."),
    53: ("1.4", "Same shape as Best Time to Buy and Sell Stock. Track the best sum ending here: "
                "max(x, best_here + x). Track the best overall."),
    228: ("1.4", "One scan. Remember where the run started. When the next number isn't +1, close the run as "
                 "\"a\" or \"a->b\"."),
    452: ("1.5", "Greedy choice. Sort by END. Shoot at the first end. Skip every balloon that starts at or before "
                 "that arrow. Next balloon: new arrow."),
    56: ("2.4", "Sort first, then one pass. Sort by start. If the next interval starts at or before the last "
                "merged end, stretch that end. Otherwise append it."),
    57: ("2.4", "Already sorted, so one pass in three phases: copy the ones that end before it, merge every "
                "overlap into it, copy the rest."),
    219: ("3.1", "A fixed window of the last k numbers, kept in a set. Seen in the set: True. Add the new one. "
                 "Once the set holds more than k, drop nums[i - k]."),
}


def lesson_order(lesson_id):
    """Sort key: '00.3' -> (0, 3); '1.8' -> (1, 8); '05' -> (5, 0)."""
    if "." in lesson_id:
        a, b = lesson_id.split(".")
        return (int(a), int(b))
    return (int(lesson_id), 0)


def unlock_of(number):
    """The lesson id (e.g. '1.4') or section number (e.g. '05') that unlocks a problem."""
    if number in EARLY:  # an early stamp never moves, even after the home section adds a lab
        return EARLY[number][0]
    if number in LABS:
        return LABS[number][0][0]
    for n, _t, _s, _d, home in PROBLEMS:
        if n == number:
            return home
    raise KeyError(number)


def url(slug):
    return f"https://leetcode.com/problems/{slug}/"


def by_number():
    return {p[0]: p for p in PROBLEMS}


def check():
    """Raise if the data is inconsistent."""
    nums = [p[0] for p in PROBLEMS]
    assert len(nums) == 150, f"expected 150 problems, found {len(nums)}"
    assert len(set(nums)) == 150, "duplicate problem numbers"
    assert len({p[2] for p in PROBLEMS}) == 150, "duplicate slugs"
    for n in list(LABS) + list(EARLY):
        assert n in set(nums), f"{n} is not in the Top 150"
    counts = {}
    for p in PROBLEMS:
        counts[p[4]] = counts.get(p[4], 0) + 1
    expected = {"01": 24, "02": 5, "03": 4, "04": 5, "05": 9, "06": 4, "07": 5, "08": 11, "09": 14,
                "10": 4, "11": 3, "12": 6, "13": 3, "14": 3, "15": 7, "16": 4, "17": 2, "18": 7,
                "19": 4, "20": 6, "21": 6, "22": 5, "23": 9}
    assert counts == expected, f"category counts differ: {counts}"
    for n, lessons in LABS.items():
        for _lesson, path in lessons:
            assert path.endswith(".py"), path
    return True


if __name__ == "__main__":
    check()
    print("OK: 150 problems, all checks pass.")
