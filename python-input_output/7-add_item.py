#!/usr/bin/python3
"""Script to add command-line arguments to a JSON file list."""

import sys
import os
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing items if file exists, otherwise start with empty list
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add command-line arguments (excluding script name)
items.extend(sys.argv[1:])

# Save updated list to file
save_to_json_file(items, filename)
