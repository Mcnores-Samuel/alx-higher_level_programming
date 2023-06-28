#!/usr/bin/python3

"""This module defines a class with a size attribute.

size is a private instance attribute.
"""


class Square:
    """Defines a size private instance attribute"""
    def __init__(self, size=0):
        """Size defined with type or value verification.

        args:
            size: integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)
