"""Rejected Olympic Sports entry.

Writes one funny single-line sport the Olympics turned down to
/output/entry.txt. The line must be 1-200 characters, a single line.
"""

import os

ENTRY = (
    "Speed Origami, 100m: Japan folded a crane in 9.58 seconds. "
    "The paper was later disqualified for doping."
)


def validate(line: str) -> str:
    """A valid entry is one non-empty line of 1-200 characters."""
    text = line.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    line = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
