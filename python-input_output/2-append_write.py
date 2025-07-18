#!/usr/bin/python3
"""Provides file append functionality with character count return."""


def append_write(filename="", text=""):
    """Appends text to a file and returns number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
