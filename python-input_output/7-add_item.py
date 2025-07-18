#!/usr/bin/python3
"""Adds command-line arguments to a JSON file list."""

import sys
import os
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing items or initialize empty list
items = []
if os.path.exists(filename):
    items = load_from_json_file(filename)

# Add command-line arguments
items.extend(sys.argv[1:])

# Save updated list
save_to_json_file(items, filename)
