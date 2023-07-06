#!/usr/bin/python3

"""This module defines a class Rectangle.

It provides methods for getting and setting with and height of a
Rectangle(width=0, height=0).
"""


class Rectangle:
    """Defines a Rectangle class for Rectangle behaviour"""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
            print(str(self.print_symbol) * self.__width, end="")
            if n != self.__height - 1:
                print()
        return ("")

    def __repr__(self):
        """Returns a string representation of the rectangle to be able to
        recreate a new instance
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Deletes the specified Rectangle object"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares two rectangle object with a bigger area

        args:
            rect_1: first rectangle object to compare
            rect_2: second rectangle object to compare with.
        Returns: a rectangle with bigger area than the other.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return (rect_1)
        elif rect_1.area() < rect_2.area():
            return (rect_2)
        else:
            return (rect_1)

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return cls(width=size, height=size)


if __name__ == "__main__":
    my_square = Rectangle.square(5)
    print("Area: {} - Perimeter: {}".format(my_square.area(),
                                            my_square.perimeter()))
    print(my_square)
