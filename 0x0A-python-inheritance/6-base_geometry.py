#!/usr/bin/python3

"""This module defines a BaseGeometry class"""


class BaseGeometry:
    """Defines a BaseGeometry class"""
    def area(self):
        """aises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    bg = BaseGeometry()
    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
