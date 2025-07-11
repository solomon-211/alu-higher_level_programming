#!/usr/bin/python3
"""Defines a Rectangle class with comprehensive features."""


class Rectangle:
    """Representation of a rectangle with advanced capabilities.

    Class Attributes:
        number_of_instances (int): Count of active instances.
        print_symbol (any): Symbol for string representation.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance."""
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
        """Calculate and return the rectangle's area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter (0 if width or height is 0)."""
        if not (self.__width and self.__height):
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return printable representation using print_symbol."""
        if not (self.__width and self.__height):
            return ""
        pattern = str(self.print_symbol) * self.__width
        return '\n'.join([pattern] * self.__height)

    def __repr__(self):
        """Return string representation for eval()."""
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        """Handle instance deletion with message and counter update."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangles by area and return the larger one
        """
        if not all(isinstance(r, Rectangle) for r in (rect_1, rect_2)):
            raise TypeError("Both must be instances of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Create a new square Rectangle instance.
        """
        return cls(size, size)
