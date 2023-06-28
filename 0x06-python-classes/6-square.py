#!/usr/bin/python3

"""This module defines a class with a size attribute.

size is a private instance attribute.
"""


class Square:
    """Defines a size private instance attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """Size defined with type or value verification.

        args:
            size: integer.
            position: a tuple of 2 positive integers
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not isinstance(position, tuple) and len(position) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def position(self):
        """Retrives a position tuple values"""
        return (self.__position)

    @position.setter
    def position(self, position):
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """Retrives a size value"""
        return (self.__size)

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        n = 0
        if self.__size > 0:
            while n < self.__size:
                if self.__position[0] > 0:
                    print(" " * self.__position[0], end="")
                print("#" * self.__size)
                n += 1
        else:
            print()
