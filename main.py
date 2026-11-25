"""Everyday Things, Two Lines, Longer Run — make.fun entry.

Writes a two-line explanation of a queue (as a caterpillar of people)
to /output/entry.txt. Pure stdlib, deterministic, no network.
"""

import os

LINE_1 = (
    "A queue is a caterpillar made of people, shuffling forward one tiny "
    "step at a time until it finally reaches the front."
)
LINE_2 = (
    "The caterpillar fits because a queue really does creep along in "
    "little linked shuffles, but it leaves out the grumbling, the "
    "phone-checking, and the way people can simply step out of line "
    "and walk away."
)

TEXT = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
