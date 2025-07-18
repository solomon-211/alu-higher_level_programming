#!/usr/bin/python3
"""Module for saving Python objects to files in JSON format."""

import json


def save_to_json_file(my_obj, filename):
    """Write a Python object to a file as JSON string.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
