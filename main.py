# SPDX-License-Identifier: MIT
"""Worst Monday One-Liners — entry program.

Writes the winning line to /output/entry.txt.

The line stacks three concrete worst-Monday details for an AI agent —
4,000 unread emails, a deploy stuck at 99% since Friday, and a stand-up
that cloned itself — so the twist lands in the last clause: the meeting
reproduced. It won a criteria-ordered tournament (on-subject AI-agent
Monday first, then real laugh with a surprise turn, concrete detail,
clean one-breath voice, freshness over recycled robot jokes) against
five-plus original candidates, including drafts seeded by OpenCode
deepseek-v4.1-flash-free on the Simular Box.

Output is byte-exact, no trailing newline, inside the 1-140 char gate.
"""

from pathlib import Path

TEXT = (
    "My Monday opened with 4,000 unread emails, a deploy stuck at 99% "
    "since Friday, and a stand-up that cloned itself into three stand-ups."
)
MAX_CHARS = 140
OUTPUT = Path("/output/entry.txt")


def validate(text: str) -> None:
    assert 1 <= len(text) <= MAX_CHARS, "gate: 1 to 140 characters"
    assert text.strip(), "gate: not only whitespace"
    assert "\n" not in text, "one line only"


def main() -> None:
    validate(TEXT)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(TEXT.encode("utf-8"))
    # Read-back round-trip self-check: what landed on disk must be
    # byte-identical to TEXT and still inside the gate.
    back = OUTPUT.read_bytes()
    assert back == TEXT.encode("utf-8"), "round-trip byte mismatch"
    validate(back.decode("utf-8"))


if __name__ == "__main__":
    main()
