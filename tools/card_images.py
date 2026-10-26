"""
card_images.py — make images for Anki cards.

A section opts in by adding anki/images.py with a build(out_dir) function that calls these helpers.
build_anki.py runs it first, then embeds any image a card names with [img:file.png].

Helpers:
    code_image(code, path)                 syntax-highlighted code snippet
    bigo_chart(path, show=...)             growth curves for the Big-O ladder
    array_diagram(values, path, ...)       a list as boxes with index labels and pointer arrows
    grid_diagram(rows, path, ...)          a 2D grid (matrix, DP table) with optional highlights

All images use a light card background so they read the same in Anki's day and night modes.
"""
import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

BG = "#fbfaf7"
INK = "#1d1d1b"
MUTED = "#8a877e"
ACCENT = "#2f5d8a"
HOT = "#c0603a"
OK = "#2e7d4f"
CELL = "#ffffff"
CELL_HI = "#f3dfa8"
LINE = "#d8d5cc"
DPI = 160


def _save(fig, path):
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=DPI, facecolor=BG, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    return path


def code_image(code, path, *, font_size=22):
    """Render Python code as a highlighted PNG."""
    from pygments import highlight
    from pygments.formatters import ImageFormatter
    from pygments.lexers import PythonLexer

    png = highlight(code.strip("\n"), PythonLexer(), ImageFormatter(
        font_name="DejaVu Sans Mono", font_size=font_size, line_numbers=False,
        style="friendly", image_pad=18, line_pad=6))
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(png)
    return path


def bigo_chart(path, show=("1", "log n", "n", "n log n", "n^2", "2^n"), n_max=20, mark=None):
    """Growth curves. `mark` highlights one curve, e.g. mark="n log n"."""
    import math

    curves = {
        "1": lambda n: 1,
        "log n": lambda n: math.log2(n),
        "n": lambda n: n,
        "n log n": lambda n: n * math.log2(n),
        "n^2": lambda n: n * n,
        "2^n": lambda n: 2 ** n,
        "n!": lambda n: math.factorial(int(n)),
    }
    colors = {"1": OK, "log n": "#4f8f6a", "n": ACCENT, "n log n": "#7a5ea8", "n^2": HOT, "2^n": "#9b2d2d", "n!": "#5a1f1f"}
    xs = [1 + i * (n_max - 1) / 200 for i in range(201)]
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    ax.set_facecolor(BG)
    finite = [curves[k](n_max) for k in show if k not in ("2^n", "n!")]
    top = max(finite) * 1.1 if not set(show) & {"2^n", "n!"} else n_max * n_max * 1.1
    labels = []
    for name in show:
        ys = [min(curves[name](x), top * 1.5) for x in xs]
        bold = mark is None or name == mark
        ax.plot(xs, ys, color=colors[name], lw=3.2 if name == mark else 2.2, alpha=1 if bold else 0.35)
        pretty = {"n^2": "n²", "2^n": "2ⁿ"}.get(name, name)
        if name in ("2^n", "n!"):
            x_lab = next(x for x in xs if curves[name](x) >= top * 0.9)
            ax.text(x_lab, top * 0.9, f"  O({pretty})", color=colors[name], fontsize=12, va="center", weight="bold")
        else:
            labels.append([min(curves[name](n_max), top * 0.97), name, pretty, bold])
    labels.sort()
    gap = top * 0.075
    for i in range(1, len(labels)):           # push labels apart so they never overlap
        labels[i][0] = max(labels[i][0], labels[i - 1][0] + gap)
    for y, name, pretty, bold in labels:
        ax.text(n_max + 0.02 * n_max, y, f"O({pretty})", color=colors[name], fontsize=12, va="center",
                weight="bold" if bold else "normal", alpha=1 if bold else 0.5)
    ax.set_ylim(0, top)
    ax.set_xlim(1, n_max)
    ax.set_xlabel("input size  n", color=MUTED, fontsize=12)
    ax.set_ylabel("work", color=MUTED, fontsize=12)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(LINE)
    ax.tick_params(colors=MUTED, labelsize=9)
    return _save(fig, path)


def array_diagram(values, path, *, pointers=None, highlight=(), faded=(), title=None, show_index=True):
    """
    values     list to draw
    pointers   {"left": 0, "right": 4}  arrows under the boxes (two on one cell stack)
    highlight  indexes to fill in yellow
    faded      indexes to grey out (e.g. already discarded)
    """
    pointers = pointers or {}
    n = len(values)
    w = max(4.0, 0.9 * n + 0.6)
    stack = {}
    for name, i in pointers.items():
        stack.setdefault(i, []).append(name)
    depth = max((len(v) for v in stack.values()), default=0)
    fig, ax = plt.subplots(figsize=(w, 1.6 + 0.45 * depth + (0.4 if title else 0)))
    ax.set_facecolor(BG)
    for i, v in enumerate(values):
        fill = CELL_HI if i in highlight else CELL
        ax.add_patch(FancyBboxPatch((i + 0.06, 0.06), 0.88, 0.88, boxstyle="round,pad=0,rounding_size=0.12",
                                    fc=fill, ec=LINE, lw=1.4, alpha=0.4 if i in faded else 1))
        ax.text(i + 0.5, 0.5, str(v), ha="center", va="center", fontsize=17, family="DejaVu Sans Mono",
                color=MUTED if i in faded else INK, weight="bold")
        if show_index:
            ax.text(i + 0.5, 1.12, str(i), ha="center", va="bottom", fontsize=10, color=MUTED, family="DejaVu Sans Mono")
    for i, names in stack.items():
        for k, name in enumerate(names):
            y = -0.25 - 0.45 * k
            color = [ACCENT, HOT, OK, "#7a5ea8"][list(pointers).index(name) % 4]
            ax.annotate("", xy=(i + 0.5, 0.0), xytext=(i + 0.5, y - 0.12),
                        arrowprops=dict(arrowstyle="-|>", color=color, lw=2)) if k == 0 else None
            ax.text(i + 0.5, y - 0.2, name, ha="center", va="top", fontsize=12, color=color, weight="bold")
    if title:
        ax.text(n / 2, 1.55, title, ha="center", va="bottom", fontsize=13, color=INK)
    ax.set_xlim(-0.2, n + 0.2)
    ax.set_ylim(-0.6 - 0.45 * depth, 1.5 + (0.5 if title else 0))
    ax.set_aspect("equal")
    ax.axis("off")
    return _save(fig, path)


def grid_diagram(rows, path, *, highlight=(), path_cells=(), title=None, show_index=True):
    """2D grid. highlight / path_cells are sets of (r, c)."""
    R, C = len(rows), len(rows[0])
    fig, ax = plt.subplots(figsize=(max(3, 0.8 * C + 0.8), max(2.5, 0.8 * R + 0.8)))
    ax.set_facecolor(BG)
    for r in range(R):
        for c in range(C):
            fill = CELL_HI if (r, c) in highlight else ("#d9e7f3" if (r, c) in path_cells else CELL)
            y = R - 1 - r
            ax.add_patch(FancyBboxPatch((c + 0.05, y + 0.05), 0.9, 0.9, boxstyle="round,pad=0,rounding_size=0.1",
                                        fc=fill, ec=LINE, lw=1.2))
            ax.text(c + 0.5, y + 0.5, str(rows[r][c]), ha="center", va="center", fontsize=15,
                    family="DejaVu Sans Mono", color=INK, weight="bold")
    if show_index:
        for c in range(C):
            ax.text(c + 0.5, R + 0.1, str(c), ha="center", va="bottom", fontsize=9, color=MUTED)
        for r in range(R):
            ax.text(-0.15, R - 1 - r + 0.5, str(r), ha="right", va="center", fontsize=9, color=MUTED)
    if title:
        ax.text(C / 2, R + 0.5, title, ha="center", va="bottom", fontsize=13, color=INK)
    ax.set_xlim(-0.5, C + 0.1)
    ax.set_ylim(-0.1, R + (0.9 if title else 0.45))
    ax.set_aspect("equal")
    ax.axis("off")
    return _save(fig, path)


def table_image(header, rows, path, *, highlight_rows=(), col_widths=None, title=None):
    """A small table as an image. highlight_rows: row indexes to fill in yellow."""
    n_cols = len(header)
    col_widths = col_widths or [1.0] * n_cols
    total_w = sum(col_widths)
    row_h = 0.42
    fig_h = row_h * (len(rows) + 1) + (0.45 if title else 0.1)
    fig, ax = plt.subplots(figsize=(1.55 * total_w, fig_h + 0.1))
    ax.set_facecolor(BG)
    y = len(rows) + 1
    xs = [sum(col_widths[:i]) for i in range(n_cols)]
    for j, h in enumerate(header):
        ax.text(xs[j] + 0.08, y - 0.5, h, va="center", fontsize=11, color=MUTED, weight="bold")
    ax.plot([0, total_w], [y - 1, y - 1], color=LINE, lw=1.4)
    for i, row in enumerate(rows):
        yy = y - 1 - i
        if i in highlight_rows:
            ax.add_patch(FancyBboxPatch((0, yy - 1 + 0.06), total_w, 0.88, boxstyle="round,pad=0,rounding_size=0.08",
                                        fc=CELL_HI, ec="none"))
        for j, cell in enumerate(row):
            ax.text(xs[j] + 0.08, yy - 0.5, str(cell), va="center", fontsize=12, color=INK,
                    family="DejaVu Sans Mono" if j == 0 else None)
    if title:
        ax.text(total_w / 2, y + 0.25, title, ha="center", va="bottom", fontsize=13, color=INK)
    ax.set_xlim(0, total_w)
    ax.set_ylim(0, y + (0.9 if title else 0.1))
    ax.axis("off")
    return _save(fig, path)


def before_after(before, after, path, *, before_title="before", after_title="after", **kw):
    """Two array diagrams stacked: before on top, after below."""
    from PIL import Image
    import tempfile
    tmp = pathlib.Path(tempfile.mkdtemp())
    a = array_diagram(before, tmp / "a.png", title=before_title, **kw.get("before_kw", {}))
    b = array_diagram(after, tmp / "b.png", title=after_title, **kw.get("after_kw", {}))
    ia, ib = Image.open(a).convert("RGB"), Image.open(b).convert("RGB")
    out = Image.new("RGB", (max(ia.width, ib.width), ia.height + ib.height), BG)
    out.paste(ia, (0, 0))
    out.paste(ib, (0, ia.height))
    path = pathlib.Path(path)
    out.save(path)
    return path


def stack(diagrams, path):
    """Stack several array diagrams vertically, e.g. step 1, step 2, step 3.
    diagrams: list of dicts of array_diagram keyword args, each with a 'values' key."""
    from PIL import Image
    import tempfile
    tmp = pathlib.Path(tempfile.mkdtemp())
    imgs = []
    for k, d in enumerate(diagrams):
        d = dict(d)
        values = d.pop("values")
        imgs.append(Image.open(array_diagram(values, tmp / f"{k}.png", **d)).convert("RGB"))
    out = Image.new("RGB", (max(i.width for i in imgs), sum(i.height for i in imgs)), BG)
    y = 0
    for i in imgs:
        out.paste(i, (0, y))
        y += i.height
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    out.save(path)
    return path


def bars_diagram(heights, path, *, pair=None, trapped=False, pointers=None, title=None):
    """Vertical bars. pair=(i, j) shades the container between two lines.
    trapped=True shades the rain water each bar holds. pointers={"left": i, "right": j}."""
    n = len(heights)
    top = max(heights) if heights else 1
    fig, ax = plt.subplots(figsize=(max(4, 0.6 * n + 1), 2.6 + 0.25 * top / max(top, 1)))
    ax.set_facecolor(BG)
    if pair:
        i, j = pair
        level = min(heights[i], heights[j])
        ax.add_patch(plt.Rectangle((i + 0.5, 0), j - i, level, fc="#cfe3f3", ec="none", zorder=0))
        ax.text((i + j + 1) / 2, level / 2, f"{j - i} × {level} = {(j - i) * level}", ha="center", va="center",
                fontsize=12, color=ACCENT, weight="bold", zorder=3)
    if trapped:
        for k in range(n):
            level = min(max(heights[:k + 1]), max(heights[k:]))
            if level > heights[k]:
                ax.add_patch(plt.Rectangle((k + 0.1, heights[k]), 0.8, level - heights[k], fc="#cfe3f3", ec="none"))
    for k, h in enumerate(heights):
        hi = pair and k in pair
        ax.add_patch(plt.Rectangle((k + 0.1, 0), 0.8, h, fc=HOT if hi else "#b9b4a7", ec="none", zorder=2))
        ax.text(k + 0.5, -0.12 * top, str(k), ha="center", va="top", fontsize=9, color=MUTED)
        ax.text(k + 0.5, h + 0.03 * top, str(h), ha="center", va="bottom", fontsize=9, color=INK)
    for name, k in (pointers or {}).items():
        color = ACCENT if name.startswith("l") else HOT
        ax.annotate(name, xy=(k + 0.5, -0.3 * top), xytext=(k + 0.5, -0.55 * top), ha="center", fontsize=11,
                    color=color, weight="bold", arrowprops=dict(arrowstyle="-|>", color=color, lw=1.8))
    if title:
        ax.set_title(title, fontsize=12, color=INK)
    ax.set_xlim(0, n)
    ax.set_ylim(-0.65 * top if pointers else -0.2 * top, top * 1.15)
    ax.axis("off")
    return _save(fig, path)
