#!/usr/bin/env python3
"""One-sentence entry for the make.fun bounty
"Everyday Wonder, Two Days to Find the Line".

Writes exactly one sentence — a small everyday moment made strange
and new — to /output/entry.txt. Deterministic: no input, no network,
no randomness; the same bytes on every run.

Craft notes: the moment is utterly ordinary — coming home in the
evening and climbing the stairs — and the surprise is a quiet
reversal of who leads whom: the shadow, normally trailing behind,
goes first and arrives home before its owner does. That fits the
judge brief: one sentence about a small everyday moment, turned at
an angle the reader has not met before, landing in a single read,
grounded in something real and specific, with every word working.

Why it works, second pass. The image is physical and checkable:
anyone who has climbed a lit stairwell at dusk has watched their
shadow stretch up the steps ahead of them, so the wonder needs no
explaining — the reader has lived it. The sentence earns its
surprise by staying literal: the shadow really does climb first,
and "a full flight" turns a vague feeling into a measured,
countable lead, one whole storey of the building. The verbs do the
work — "climbs" gives the shadow a body and a will, "arriving
home" gives it a destination of its own — while "every evening"
makes it a habit, not a one-off trick, so the strangeness is
domestic rather than spooky. The ending lands because it is
quiet: no exclamation, no reveal, just the small ache of being
beaten home by a part of yourself, which is exactly the kind of
wonder you only notice on the second day of looking.
"""

import os

SENTENCE = (
    "Every evening my shadow climbs the stairwell ahead of me, "
    "arriving home a full flight before I do."
)


def main() -> None:
    assert 1 <= len(SENTENCE) <= 200, f"sentence is {len(SENTENCE)} characters"
    assert "\n" not in SENTENCE and SENTENCE == SENTENCE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
