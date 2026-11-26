"""One-Liner Laughs (u-coral-404-one-liner-laughs-aa872d41).

Writes the tournament-winning one-line joke to /output/entry.txt.
The winning line was selected from 42 candidates in a scored head-to-head
tournament judged against the comedy-club-headliner brief (see README.md).
"""

import os

WINNING_LINE = (
    'My resume says I\'m a team player. '
    'My browser history says I googled "how to work alone" twelve times.'
)


def main() -> None:
    # Gate pre-check: the winning line must be 1-200 chars, not only whitespace.
    line = WINNING_LINE
    if not (1 <= len(line) <= 200) or not line.strip():
        raise ValueError(f"winning line fails the gate: {len(line)} chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Read-back verification: re-check the exact winning line and its char count.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise ValueError("read-back mismatch: entry.txt differs from WINNING_LINE")
    if len(written) != 101:
        raise ValueError(f"read-back char count {len(written)} != 101")


if __name__ == "__main__":
    main()
