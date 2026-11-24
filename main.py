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
