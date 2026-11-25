"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Entry (one sentence, 130 characters, gate 1-280):

    Every summer evening we chased fireflies past the fence until the
    streetlights buzzed on and Mum called us home by our full names.

Decision record
---------------
Candidates weighed against the judge's criteria, in order (nostalgia first,
then concrete place/time/sensation, then honest small detail, then a tight
single sentence, then a lingering warm ache):

A. Grandmother's kitchen / fresh rice:
   "Grandma's kitchen always smelled of fresh rice and woodsmoke, and I
   was never allowed to stir the pot until the steam stopped burning my
   face."
   Loses: the brief itself offers "the smell of fresh rice" as its example,
   so the field will be crowded with rice-and-kitchen lines; it risks
   reading as the brief's echo rather than a memory of its own. The steam
   detail is honest, but the sentence has no ending ache -- it just stops.

B. Summer evenings / fireflies (CHOSEN):
   "Every summer evening we chased fireflies past the fence until the
   streetlights buzzed on and Mum called us home by our full names."
   Wins: a concrete time (summer evening) and place (past the fence), two
   sensations (fireflies, streetlights buzzing on), and the small honest
   detail that proves it happened -- being called home by your full names,
   which every child knows means the day is over. The ache lands in the
   last words: home, called, full names.

C. Rain on the tin roof:
   "When the rain started on the tin roof, my father would lift me onto
   his shoulders so I could watch the street turn into a river from the
   doorway."
   Strong reserve: the tin roof and the street turning into a river are
   vivid and true. Loses to B because its warmth is in the father's lift,
   a single image, while B's ache is the whole evening ending -- the
   nostalgia criterion weighs the ending more than the image.

D. The ice-cream man:
   "The ice-cream man rang his bell at three o'clock sharp, and we traded
   bottle caps for the last red popsicle as if it were gold."
   Loses: bottle caps and the red popsicle are honest details, but the
   sentence is a charming anecdote rather than a memory that aches -- it
   ends on a joke ("as if it were gold") instead of on the feeling of
   childhood slipping away.

Writing passes (Pass 2, genuine revisions to the winner):
1. First draft ended flat: "...until the streetlights came on and Mum
   called us home."  "Came on" is a dead verb with no sensation, so it
   became "buzzed on" -- a sound the reader can hear, which grounds the
   memory in a concrete sensation (criterion 2) and makes the evening
   feel like a real place rather than a postcard.
2. The draft also ended on "called us home", which states the ending
   without earning it. Adding "by our full names" gives the sentence its
   honest small detail (criterion 3): no child is called by their full
   name unless the day is truly over. A longer variant was tried and
   dropped -- "...and Mum called us home by our full names, one by one,
   and the fireflies kept going without us" -- because the extra clause
   explains the ache instead of letting the last words carry it.

Pass 3 (revision pass, output line unchanged):
   The gate claimed "exactly one sentence" but never counted sentences --
   it only rejected newlines. A count_sentences() helper was added and
   wired into check_gate, so the one-sentence claim is now actually
   enforced (ENTRY has exactly one terminator: its final full stop).
   A leading/trailing-whitespace guard was added for the same reason:
   stray spaces around the line would survive the old checks. ENTRY
   itself was not touched -- same 130 characters, same single sentence --
   and the line written to /output/entry.txt is byte-identical to before.
"""

import os

ENTRY = (
    "Every summer evening we chased fireflies past the fence until the "
    "streetlights buzzed on and Mum called us home by our full names."
)

MAX_CHARS = 280


def count_sentences(text):
    """Count sentence terminators (., !, ?) in the stripped text.

    The entry is one sentence, so exactly one terminator is expected --
    the final full stop. Any extra terminator means a second sentence
    slipped in, even if the text is still a single line.
    """
    return sum(1 for ch in text.strip() if ch in ".!?")


def check_gate(text):
    """Mirror the sealed gate: 1-280 UTF-8 chars, not only whitespace,
    exactly one sentence (a single line)."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-280 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    if count_sentences(text) != 1:
        raise ValueError(
            "entry must be exactly one sentence, got %d"
            % count_sentences(text)
        )
    return True


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    check_gate(ENTRY)
    path = entry_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
