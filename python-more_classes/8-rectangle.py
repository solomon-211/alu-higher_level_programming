#!/usr/bin/python3
"""Rectangle class with dimensions, display, and comparison features."""


class Rectangle:
    """Represents a rectangle with width, height, and comparison methods."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize dimensions and increment instance count."""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Validate and set width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Validate and set height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return width * height."""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter or 0 if either dimension is 0."""
        if not self.__width or not self.__height:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation using print_symbol."""
        if not self.__width or not self.__height:
            return ""
        symbol_line = str(self.print_symbol) * self.__width
        return '\n'.join([symbol_line for _ in range(self.__height)])

    def __repr__(self):
        """Return string that can recreate the instance."""
        return (f"{self.__class__.__name__}"
                f"({self.__width}, {self.__height})")

    def __del__(self):
        """Decrement instance count and print deletion message."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return rectangle with larger area (rect_1 if equal)."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
