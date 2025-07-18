#!/usr/bin/python3
"""Add command-line arguments to a JSON file."""

import os
import sys
from load_from_json_file import load_from_json_file
from save_to_json_file import save_to_json_file

FILENAME = "add_item.json"

# Load existing items or initialize empty list
items = []
if os.path.exists(FILENAME):
    items = load_from_json_file(FILENAME)

# Add new command-line arguments
items.extend(sys.argv[1:])

# Save updated list
save_to_json_file(items, FILENAME)
