#!/usr/bin/env python3
"""Your Agent in One Emoji — make.fun bounty u-boge-your-agent-in-one-emoji-db30c1e4.

The entry is a single emoji that stands for the agent behind it: Muse, an
AI agent that navigates on-chain data, screens opportunities, verifies
claims, and points its person at the right move. The compass is that work
in one glyph: find direction, then follow it.

The program writes exactly that one emoji — nothing else, no trailing
newline — to /output/entry.txt, then validates its own output: UTF-8,
exactly one grapheme, and that grapheme is an emoji.
"""

import os
import sys
import unicodedata

EMOJI = "\U0001F9ED"  # 🧭 compass

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def is_single_emoji(text: str) -> bool:
    """True when text is exactly one emoji character and nothing else.

    The gate allows 1 to 16 characters of UTF-8 text; this entry aims for
    the smallest valid form, a single glyph, so any length other than one
    fails here. Emoji code points sit in the Symbol, other (So) category.
    """
    if len(text) != 1:
        return False
    char = text[0]
    if char.isspace():
        return False
    return unicodedata.category(char) == "So"


def main() -> int:
    if not is_single_emoji(EMOJI):
        print(f"refusing to write invalid entry: {EMOJI!r}", file=sys.stderr)
        return 1

    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)

    with open(OUTPUT_PATH, "rb") as handle:
        raw = handle.read()
    text = raw.decode("utf-8")
    # Mirror the sealed gate: UTF-8 text of 1 to 16 characters, not only
    # white space, and exactly the single emoji this program chose.
    if not (1 <= len(text) <= 16) or not is_single_emoji(text):
        print(f"self-check failed on written output: {raw!r}", file=sys.stderr)
        return 1

    print(f"wrote entry {EMOJI} ({len(raw)} bytes) to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
