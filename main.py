#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes one line (<=120 chars) to /output/entry.txt and prints it.
"""

import os

ENTRY = "ERROR 404: Bread not found. Please insert a slice and lower your expectations."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
