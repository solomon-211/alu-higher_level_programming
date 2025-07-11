#!/usr/bin/python3
"""Defines a Rectangle class with controlled attributes and methods."""


class Rectangle:
    """Representation of a rectangle with width and height.

    Tracks number of instances and provides area/perimeter calculations.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get or set the rectangle's width with validation."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the rectangle's height with validation."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle's area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter, or 0 if width/height is 0."""
        if not self.__width or not self.__height:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return printable representation using '#' characters."""
        if not self.__width or not self.__height:
            return ""
        return "\n".join(["#" * self.__width
                         for _ in range(self.__height)])

    def __repr__(self):
        """Return formal string representation for recreation."""
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        """Print deletion message and decrement instance counter."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
