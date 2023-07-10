#!/usr/bin/python3

"""This module defines a BaseGeometry class"""


class BaseGeometry:
    """Defines a BaseGeometry class"""
    def area(self):
        """aises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value to be an integer and greater than 0"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
