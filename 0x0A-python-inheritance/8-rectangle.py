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


if __name__ == "__main__":
    r = Rectangle(3, 5)
    print(r)
    print(dir(r))
    try:
        print("Rectangle: {} - {}".format(r.width, r.height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r2 = Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
