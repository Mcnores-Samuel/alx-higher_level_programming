#!/usr/bin/python3

"""This module define a Base subclass (Rectangle) which
inherits from Base class
"""
from models.base import Base


class Rectangle(Base):
    """Defines Rectangle class, a subclass of Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle object

        args:
            width: represents the width of the rectangle object.
            height: represents the height of the rectangle object.
            x: an integer for space pretty printing
            y: an integer for space pretty printing
        """
        super().__init__(id)
        if type(width) is not int and type(width) == bool:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int and type(height) == bool:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__heigth = height
        if type(x) is not int and type(x) == bool:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int and type(y) == bool:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, width):
        if type(width) is not int and type(width) == bool:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return (self.__heigth)

    @height.setter
    def height(self, height):
        if type(height) is not int and type(height) == bool:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__heigth = height

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, x):
        if type(x) is not int and type(x) == bool:
            raise TypeError("width must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, y):
        if type(y) is not int and type(y) == bool:
            raise TypeError("width must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
