#!/usr/bin/python3

"""This module defines a Square class and also inherits
from Rectangle class in the 9-rectangle module.
"""
Rectangle = __import__("9-rectangle").Rectangle


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
