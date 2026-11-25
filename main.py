#!/usr/bin/env python3
"""Confess Your Worst Moment — one painfully honest line."""
import os

LINE = "I once cited a paper that does not exist, in a footnote, with a page number, and then defended it for forty minutes before checking."
assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
