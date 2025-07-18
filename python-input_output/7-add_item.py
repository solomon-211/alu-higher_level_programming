#!/usr/bin/python3
"""Script to add command-line arguments to a JSON file."""

import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing items or create empty list
if path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add command-line arguments
items.extend(sys.argv[1:])

# Save updated list
save_to_json_file(items, filename)
