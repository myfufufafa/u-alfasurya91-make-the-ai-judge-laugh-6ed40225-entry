#!/usr/bin/env python3
"""Make the AI Judge Laugh — one original office-life joke, one line.

Writes the joke to /output/entry.txt (UTF-8, 1-200 chars, single line).
Stdlib only, fully deterministic: same output on every run.

The joke is written from scratch for this entry: a true office
observation (the printer that only breaks before a deadline) with a
surprising last word (it reports to management).
"""

import os

JOKE = (
    "The office printer only jams when a deadline is five minutes away "
    "\u2014 I'm starting to think it reports to management."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "joke must be a single line"
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
