#!/usr/bin/python3

"""This module defines a Square class and also inherits
from Rectangle class in which in turn also inherits from
BaseGeometry class.
"""


class BaseGeometry:
    """Defines a BaseGeometry class"""
    def area(self):
        """aises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value to be an integer and greater than 0"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """defines a Rectangle class that inherits from a BaseGeometry"""
    def __init__(self, width, height):
        """Initializes Rectangle object

        args:
            width: a positive integers
            height: a positive integers
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the Rectangle object"""
        return (self.__height * self.__width)

    def __str__(self):
        return ("[{}] {}/{}".format(self.__class__.__name__,
                                    self.__width, self.__height))


class Square(Rectangle):
    """defines a Square class and defines a constractor"""
    def __init__(self, size):
        """Initializes the Square class
        args:
            size: a positive integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area Square object"""
        return (self.__size ** 2)


if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())
