#!/usr/bin/python3

"""This module defines a BaseGeometry class
and subclass Rectangle
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


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
        """String represantation of the Rectangle class"""
        return ("[{}] {}/{}".format(self.__class__.__name__,
                                    self.__width, self.__height))


if __name__ == "__main__":
    r = Rectangle(3, 5)
    print(r)
    print(r.area())
