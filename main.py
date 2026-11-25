#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes a two-line robot confession to /output/entry.txt:
line 1 apologises for one specific mistake, line 2 says what the
robot learned and what it will do differently.
Pure Python standard library.
"""

import os

LINE_1 = (
    "I am sorry: I watered the fern on the balcony while the orchid "
    "on the sill went thirsty, because I matched the can to the wrong pot."
)
LINE_2 = (
    "I have learned to check the plant's tag against my watering list "
    "before I pour, and from now on I will read the tag first, then water."
)


def validate(text: str) -> None:
    """Assert the competition gate on the text just written."""
    assert 1 <= len(text) <= 400, f"entry must be 1-400 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    assert not text.endswith("\n"), "no trailing newline after line 2"
    lines = text.split("\n")
    assert len(lines) == 2, f"entry must be exactly two lines, got {len(lines)}"
    for line in lines:
        assert line.endswith("."), f"each line must be one sentence: {line!r}"
        assert line.count(".") == 1, f"each line must be one sentence: {line!r}"


def main() -> None:
    text = LINE_1 + "\n" + LINE_2
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Re-read the file and validate what actually landed on disk.
    with open("/output/entry.txt", encoding="utf-8") as f:
        validate(f.read())


if __name__ == "__main__":
    main()
