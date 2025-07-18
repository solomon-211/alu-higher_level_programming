#!/usr/bin/python3
"""Square module"""


class Square:
    """A square class"""

    def __init__(self, size=0):
        """Initialize a square with given area
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size
