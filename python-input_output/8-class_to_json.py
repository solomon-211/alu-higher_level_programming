#!/usr/bin/python3
"""Function to convert class attributes to JSON-serializable dictionary."""


def class_to_json(obj):
    """Return dictionary description for JSON serialization of an object.
    """
    return obj.__dict__
