#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day — writes one roast line
to /output/entry.txt.

The roast: my phone, which has 128 gigs of storage and still begs me
to delete photos — a hoarder with a flagship budget. Switched from
the smartwatch draft: the storage complaint is the flaw every judge
has felt in their own pocket.
"""
import os

ROAST = "My phone has 128 gigs of storage and still begs me to delete photos, like a hoarder asking for a bigger house."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")

if __name__ == "__main__":
    main()
