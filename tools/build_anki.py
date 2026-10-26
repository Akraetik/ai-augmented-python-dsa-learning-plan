"""
build_anki.py — build a section's Anki deck from anki/cards.py.

cards.py defines:
    DECK = "00 Foundations"
    CARDS = {"Subdeck name": [(front, back, "tag1 tag2"), ...], ...}

Text formatting inside fronts/backs:
    `code`            -> inline code
    ```...```         -> code block
    **bold**          -> bold
    lines starting "- " -> bullet list
    [img:name.png]    -> an image (own line). File lives in anki/images/.

Images: if anki/images.py exists, its build(out_dir) runs first to (re)draw images into anki/images/
using tools/card_images.py. Media files are renamed dsa-sNN-<name> inside the deck so they never
clash with other decks in your Anki collection.

Output:  anki/section-NN.apkg  and  anki/section-NN.csv
IDs are deterministic, so rebuilding and re-importing updates cards instead of duplicating them.

Usage:  python tools/build_anki.py sections/00-foundations
"""
import csv
import hashlib
import html
import importlib.util
import pathlib
import re
import sys

import genanki

ROOT_DECK = "DSA Mastery"
MODEL_ID = 1735200001  # fixed forever: every section shares one note type

CSS = """
.card{font-family:-apple-system,Segoe UI,Roboto,sans-serif;font-size:19px;line-height:1.45;text-align:left;
      color:#1d1d1b;background:#f7f6f2;padding:18px;max-width:640px;margin:0 auto}
.nightMode.card,.night_mode .card{color:#ecebe6;background:#1d1d1b}
.front{font-weight:600}
.tag{font-size:12px;letter-spacing:.05em;text-transform:uppercase;color:#8a877e;margin-bottom:10px}
code{font-family:Consolas,Menlo,monospace;background:rgba(127,127,127,.15);padding:1px 5px;border-radius:4px;font-size:.92em}
pre{font-family:Consolas,Menlo,monospace;font-size:15px;line-height:1.4;background:rgba(127,127,127,.13);
    padding:10px 12px;border-radius:8px;overflow-x:auto;white-space:pre}
hr#answer{border:none;border-top:1px solid rgba(127,127,127,.35);margin:16px 0}
ul{margin:6px 0 6px 20px;padding:0}li{margin:3px 0}
.img{margin:10px 0;text-align:center}.img img{max-width:100%;height:auto;border-radius:8px;border:1px solid rgba(127,127,127,.25)}
b{color:#2f5d8a}.nightMode b,.night_mode b{color:#8fbbe6}
"""

MODEL = genanki.Model(
    MODEL_ID,
    "DSA Mastery Card",
    fields=[{"name": "Front"}, {"name": "Back"}, {"name": "Topic"}],
    templates=[{
        "name": "Card 1",
        "qfmt": '<div class="tag">{{Topic}}</div><div class="front">{{Front}}</div>',
        "afmt": '<div class="tag">{{Topic}}</div><div class="front">{{Front}}</div><hr id="answer">{{Back}}',
    }],
    css=CSS,
)


def did(name):
    return int(hashlib.sha1(name.encode()).hexdigest()[:8], 16)


IMG = re.compile(r"^\[img:([\w.\-]+)\]$")
MEDIA_PREFIX = ""   # set per section in main()
USED_MEDIA = set()


def fmt(text):
    """Tiny markdown to HTML for cards."""
    text = text.strip("\n")
    blocks = re.split(r"```(?:python)?\n?(.*?)```", text, flags=re.S)
    out = []
    for i, part in enumerate(blocks):
        if i % 2 == 1:
            out.append("<pre>" + html.escape(part.rstrip("\n")) + "</pre>")
            continue
        lines = part.split("\n")
        buf, in_list = [], False
        for line in lines:
            im = IMG.match(line.strip())
            if im:
                if in_list:
                    buf.append("</ul>")
                    in_list = False
                media = MEDIA_PREFIX + im.group(1)
                USED_MEDIA.add((im.group(1), media))
                buf.append(f'<div class="img"><img src="{media}"></div>')
                continue
            esc = html.escape(line)
            esc = re.sub(r"`([^`]+)`", r"<code>\1</code>", esc)
            esc = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", esc)
            if line.startswith("- "):
                if not in_list:
                    buf.append("<ul>")
                    in_list = True
                buf.append("<li>" + esc[2:] + "</li>")
            else:
                if in_list:
                    buf.append("</ul>")
                    in_list = False
                if esc.strip():
                    buf.append(esc + "<br>")
        if in_list:
            buf.append("</ul>")
        out.append("".join(buf))
    result = "".join(out)
    return re.sub(r"(<br>)+$", "", result)


def main(section):
    section = pathlib.Path(section)
    spec = importlib.util.spec_from_file_location("cards", section / "anki" / "cards.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)

    num = section.name.split("-")[0]
    global MEDIA_PREFIX
    MEDIA_PREFIX = f"dsa-s{num}-"
    USED_MEDIA.clear()
    img_dir = section / "anki" / "images"
    img_script = section / "anki" / "images.py"
    if img_script.exists():
        sys.path.insert(0, str(pathlib.Path(__file__).parent))
        spec_i = importlib.util.spec_from_file_location("images", img_script)
        mi = importlib.util.module_from_spec(spec_i)
        spec_i.loader.exec_module(mi)
        mi.build(img_dir)
    decks, rows, fronts = [], [], set()
    for sub, cards in m.CARDS.items():
        name = f"{ROOT_DECK}::{m.DECK}::{sub}"
        deck = genanki.Deck(did(name), name)
        for front, back, tags in cards:
            key = f"{num}|{sub}|{front}"
            assert front not in fronts, f"duplicate front: {front}"
            assert back.strip(), f"empty back: {front}"
            fronts.add(front)
            tag_list = [f"s{num}"] + tags.split()
            note = genanki.Note(model=MODEL, fields=[fmt(front), fmt(back), f"{m.DECK} · {sub}"],
                                tags=tag_list, guid=genanki.guid_for(key))
            deck.add_note(note)
            rows.append([fmt(front), fmt(back), f"{m.DECK}::{sub}", " ".join(tag_list)])
        decks.append(deck)

    out = section / "anki" / f"section-{num}.apkg"
    media_files = []
    if USED_MEDIA:
        import shutil
        import tempfile
        tmp = pathlib.Path(tempfile.mkdtemp())
        for src_name, media in sorted(USED_MEDIA):
            src = img_dir / src_name
            assert src.exists(), f"card names missing image: {src}"
            shutil.copy(src, tmp / media)
            media_files.append(str(tmp / media))
    pkg = genanki.Package(decks)
    pkg.media_files = media_files
    pkg.write_to_file(str(out))
    with open(section / "anki" / f"section-{num}.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["front", "back", "deck", "tags"])
        w.writerows(rows)
    print(f"built {out.name}: {len(rows)} cards in {len(decks)} subdecks, {len(media_files)} images")


if __name__ == "__main__":
    main(sys.argv[1])
