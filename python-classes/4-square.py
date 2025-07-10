#!/usr/bin/python3
"""Square module"""


class Square:
    """A square class"""

    def __init__(self, size=0):
        """Initialize a square with given size
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area
        """
        return self.__size * self.__size
