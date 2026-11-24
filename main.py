#!/usr/bin/env python3
"""Two Days of Excuses.

Writes the funniest one-line excuse an AI gives for a missed deadline,
under 200 characters, to /output/entry.txt. The joke is the gap between a
machine's total confidence and its total failure: it was 100% sure it had
already finished — and 100% wrong about that too.
"""

EXCUSE = (
    "I missed the deadline because I was 100% certain I had already "
    "finished it, and 100% wrong about that too."
)
LIMIT = 200
OUTFILE = "/output/entry.txt"


def excuse_line():
    line = EXCUSE.strip()
    assert line, "excuse must not be empty"
    assert "\n" not in line, "excuse must be one line"
    assert len(line) < LIMIT, f"excuse is {len(line)} chars, must be under {LIMIT}"
    return line


def main():
    line = excuse_line()
    with open(OUTFILE, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"excuse written: {len(line)} chars")


if __name__ == "__main__":
    main()
