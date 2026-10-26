# Tools

| Script | What it does | Who uses it |
|---|---|---|
| `_check.py` | Test runner every lab imports. A copy sits in each `labs/` folder. | Learners (automatically) |
| `run_labs.py` | Runs every lab in a section and prints a scoreboard. | Learners |
| `verify_solutions.py` | Checks each official solution passes and each starter fails. | Maintainers |
| `build_anki.py` | Builds `anki/section-NN.apkg` and `.csv` from `anki/cards.py`. Runs `anki/images.py` first if present. | Maintainers |
| `card_images.py` | Draws card images: code snippets, Big-O charts, array/grid diagrams, tables, before/after. | Maintainers |
| `build_quiz.py` | Builds `quiz.html`, `quiz.md`, `quiz_answers.md` from `quiz/quiz_data.py`. | Maintainers |
| `build_review.py` | Rebuilds `review/quiz.html` and the tapered review audio scripts from every section. | Maintainers |
| `review.py` | `python tools/review.py NN` — copies this week's tapered cold solves into `review/cold-solves/`. | Learners |
| `build_audio.py` | Renders `audio/scripts/*.txt` to MP3 with Kokoro TTS, plus transcripts. | Maintainers |

## Audio setup

```
pip install kokoro-onnx soundfile numpy
```

Download `kokoro-v1.0.onnx` and `voices-v1.0.bin` from the
[kokoro-onnx releases](https://github.com/thewh1teagle/kokoro-onnx/releases) (tag `model-files-v1.0`)
into `tools/models/`. Install ffmpeg. Then:

```
python tools/build_audio.py sections/01-array-string
```

Voices: narrator `am_michael`, answer voice `af_heart`. Change them at the top of `build_audio.py`.
Pronunciation fixes live in the `SAY` list in the same file.

## Card images

1. In the section, create `anki/images.py` with a `build(out)` function that calls helpers from `card_images.py`.
2. In `anki/cards.py`, put `[img:file.png]` on its own line in a card's front or back.
3. Run `build_anki.py`. It draws the images into `anki/images/` and packs them into the `.apkg`.

See `sections/00-foundations/anki/images.py` for examples of every helper.

## Script format

```
# Track title
N: Narrator line.
A: Answer-voice line.
[pause 3]
```

## Adding a section

1. Copy `sections/01-array-string` as a template.
2. Write lessons, labs (each with `ENTRY`, `run_tests`), solutions (`lab_xx_solution.py`).
3. `python tools/verify_solutions.py sections/NN-name` until every lab says OK.
4. Write `anki/cards.py`, `quiz/quiz_data.py`, `audio/scripts/*.txt`. Run the three build scripts.
5. Copy `tools/_check.py` into the new `labs/` folder.
