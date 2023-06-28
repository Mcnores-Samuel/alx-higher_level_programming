#!/usr/bin/python3

"""This module defines a class with a size attribute.

size is an instance attribute with no type or value verification for now.
"""


class Square:
    """Defines a size private instance attribute"""
    def __init__(self, size):
        """Size defined with no type or value verification"""
        self.__size = size
