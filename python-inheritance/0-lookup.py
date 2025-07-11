#!/usr/bin/python3
"""
Module for inspecting object attributes and methods.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    return sorted(dir(obj))
