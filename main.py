#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown — writes one title to /output/entry.txt.

The title sounds like a real job because it wears a real corporate shape —
Senior Vice President of — and then the department is gloriously wrong:
apologizing to the cloud. You can picture the person doing it, in a suit,
on a call, saying sorry to a server rack that never answers back. One
specific twist, readable at a glance, funny on the first read.
"""

import os

LINE = "Senior Vice President of Apologizing to the Cloud"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
