#!/usr/bin/python3
"""Module to read and print a file."""


def read_file(filename=""):
    """Read a UTF-8 file and print its contents."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
