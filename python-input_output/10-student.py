#!/usr/bin/python3
"""Defines a Student class with selective JSON serialization."""


class Student:
    """Represents a student with customizable JSON conversion."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the Student instance."""
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {
                    attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)
                    }
        return self.__dict__
