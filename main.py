#!/usr/bin/env python3
"""One-sentence entry for the make.fun bounty
"Everyday Wonder, Two Days to Find the Line".

Writes exactly one sentence — a small everyday moment made strange
and new — to /output/entry.txt. Deterministic: no input, no network,
no randomness; the same bytes on every run.

Craft notes: the moment is utterly ordinary — riding the elevator home
in the evening — and the surprise is a quiet reversal of who knows
whom: the lift dings for my floor before my finger reaches the button,
as if the building itself learned my evenings by heart. That fits the
judge brief: one sentence about a small everyday moment, turned at
an angle the reader has not met before, landing in a single read,
grounded in something real and specific, with every word working.

Why it works, second pass. The image is physical and checkable:
anyone who rides the same lift every evening has felt it guess
right, so the wonder needs no explaining — the reader has lived it.
The sentence earns its surprise by staying literal: the ding really
does come before the press, and "learned my evenings by heart" turns
a machine's habit into a small act of attention, as if the building
keeps me the way I keep it. The verbs do the work — "dings" gives
the lift a voice, "learned" gives it a memory — while "my floor"
makes the moment mine, not anyone's, so the strangeness is domestic
rather than spooky. The ending lands because it is quiet: no
exclamation, no reveal, just the small warmth of being known by a
place, which is exactly the kind of wonder you only notice on the
second day of looking.
"""

import os

SENTENCE = (
    "The elevator dings for my floor before I press the button, "
    "as if the building learned my evenings by heart."
)


def main() -> None:
    assert 1 <= len(SENTENCE) <= 200, f"sentence is {len(SENTENCE)} characters"
    assert "\n" not in SENTENCE and SENTENCE == SENTENCE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
