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

    def area(self):
        """Returns the area of the Rectangle object"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the Rectangle object"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """Provides a String representation of the object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        for n in range(self.__height):
            print("#" * self.__width, end="")
            if n != self.__height - 1:
                print()
        return ("")

    def __repr__(self):
        """Returns a string representation of the rectangle to be able to
        recreate a new instance
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(str(my_rectangle))
    print("--")
    print(my_rectangle)
    print("--")
    print(repr(my_rectangle))
    print("--")
    print(hex(id(my_rectangle)))
    print("--")
    new_rectangle = eval(repr(my_rectangle))
    print(str(new_rectangle))
    print("--")
    print(new_rectangle)
    print("--")
    print(repr(new_rectangle))
    print("--")
    print(hex(id(new_rectangle)))
    print("--")
    print(new_rectangle is my_rectangle)
    print(type(new_rectangle) is type(my_rectangle))
