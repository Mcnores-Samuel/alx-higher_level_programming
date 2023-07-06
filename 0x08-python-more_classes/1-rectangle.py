#!/usr/bin/python3

"""This module defines a class Rectangle.

It provides methods for getting and setting with and height of a
Rectangle(width=0, height=0).
"""


class Rectangle:
    """Defines a Rectangle class for Rectangle behaviour"""
    def __init__(self, width=0, height=0):
        """Initializes the Rectangle object.

        args:
            width(integer): width of the Rectangle object
            height(integer): height of the Rectangle object
        Returns: None
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """Returns the width of the Rectangle object"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set a width value or Initializes the width value
        of the object.

        args:
            value(integer): a value for the width of the Rectangle object.
        Returns: None
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns The height of the Rectangle object"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets or Initializes the height value of the Rectangle
        object.

        args:
            value(integer): integer value for the height of the Rectangle
            object.
        Returns: None
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)
    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
