#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single vending-machine pickup line to entry.txt.
Deterministic: the same line, byte for byte, on every run.

Output location: $MAKEFUN_OUTPUT_DIR/entry.txt when MAKEFUN_OUTPUT_DIR
is set (used for local verification so runs stay isolated), otherwise
/output/entry.txt, the path the grader reads.

The line (117 characters):
  Press B4 -- I've been saving the last chocolate bar just for you.
  Fair warning: my coil drops fast, but I fall harder.

Why this line: it is spoken by the machine itself ("Press B4", "my coil"),
it lives in the machine's own world (slot B4, coil, chocolate bar), the
punch lands on the last few words ("but I fall harder"), and it stays
cheeky and warm rather than creepy.
"""

import os

LINE = "Press B4 \u2014 I\u2019ve been saving the last chocolate bar just for you. Fair warning: my coil drops fast, but I fall harder."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
