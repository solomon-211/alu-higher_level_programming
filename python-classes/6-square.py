#!/usr/bin/python3
"""Square module"""


class Square:
    """A square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with given size and position

        Args:
            size: The size of the square (default: 0)
            position: The position of the square (default: (0, 0))

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers
            ValueError: If size is less than 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square

        Args:
            value: The new size value

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square

        Returns:
            tuple: The position of the square as (x, y)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square

        Args:
            value: The new position value

        Raises:
            TypeError: If position is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area

        Returns:
            int: The area of the square (size * size)
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the character #

        If size is 0, prints an empty line
        Position is used to add spaces before the square
        """
        if self.__size == 0:
            print()
            return
            
        # Print vertical offset (position[1] new lines)
        for i in range(self.__position[1]):
            print()
        
        # Print the square with horizontal offset (position[0] spaces)
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
