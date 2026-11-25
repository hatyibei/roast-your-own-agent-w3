#!/usr/bin/env python3
"""Entry for make.fun's "Roast Your Own Agent".

Writes a single roast line about my own AI agent to /output/entry.txt
(UTF-8, 1-200 characters, no trailing newline).
"""
import os

ENTRY = (
    "My agent read the whole internet, aced every benchmark, and still "
    "needs me to prove I'm not a robot by finding traffic lights."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
