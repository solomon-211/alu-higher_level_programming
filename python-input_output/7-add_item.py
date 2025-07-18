#!/usr/bin/python3
"""
Module for adding items to a JSON file.

This module provides functionality to add command-line arguments as items
to a JSON file. It loads existing items from the file (if it exists),
adds new items from command-line arguments, and saves the updated list
back to the file.

Usage:
    python3 add_item.py item1 item2 item3

The items will be added to 'add_item.json' file.
"""

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
