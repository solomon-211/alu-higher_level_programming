#!/usr/bin/python3
"""Module containing class_to_json function for serialization."""


def class_to_json(obj):
    """Returns dictionary description for JSON serialization of an object.

    Args:
        obj: Instance of a class with serializable attributes

    Returns:
        dict: Dictionary containing object's serializable attributes
    """
    return obj.__dict__
