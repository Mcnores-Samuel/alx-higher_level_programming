#!/usr/bin/python3

"""This module define Base class for all subclasses"""


class Base:
    """Base class definition"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the Base class with id public instance attribute

        args:
            id: an integer.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
