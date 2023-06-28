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
        try:
            self.__size = size
            if self.__size is not isinstance(self.__size, int):
                raise TypeError
            if self.__size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
