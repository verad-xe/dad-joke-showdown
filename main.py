#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt.
The joke is the whole entry: at most 200 characters, UTF-8 text.
The output is fully deterministic: the same joke, byte for byte, on
every run, with no input, no network and no randomness.
"""

import os

JOKE = (
    "I told the kids I'm starting a band called The Leftovers. "
    "We only play covers \u2014 and only on Sundays, right after dinner."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
