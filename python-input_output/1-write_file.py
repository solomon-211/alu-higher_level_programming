#!/usr/bin/python3
"""Module containing a function to write a string to a file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return the numbers count
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
