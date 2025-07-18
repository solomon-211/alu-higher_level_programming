#!/usr/bin/python3
"""Defines a Student class with JSON serialization capability."""


class Student:
    """Represents a student with basic information and JSON conversion."""
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of the Student instance.
        """
        return self.__dict__
