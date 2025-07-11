#!/usr/bin/python3
"""Rectangle class with width, height, print symbol, and instance tracking."""


class Rectangle:
    """Represents a rectangle with dimensions and customizable display."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional dimensions."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with integer and non-negative validation."""
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
        """Set height with integer and non-negative validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area (width * height)."""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter or 0 if either dimension is 0."""
        if 0 in (self.__width, self.__height):
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string of rectangle using print_symbol."""
        if 0 in (self.__width, self.__height):
            return ""
        pattern = str(self.print_symbol) * self.__width
        return '\n'.join([pattern for _ in range(self.__height)])

    def __repr__(self):
        """Return string representation for eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Handle instance deletion."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
