#!/usr/bin/python3

"""This module define a Square class which inherits from
Rectangle class, a subclass of Base class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines the Square class and inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes both the Square class and the Rectangle parent class

        args:
            size(integer): represents the size of the Square object
            x: an integer for space representation
            y: an integer
            id: id for the the current Square object
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size of the Square object"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Sets or initializes width and height of the Square object

        args:
            value: an integer for both width and height of the Square
            object.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of the Square object"""
        result = "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                               self.id, self.x, self.y,
                                               self.size)
        return (result)

    def area(self):
        """Returns the area of the Square object"""
        return (self.size ** 2)

    def update(self, *args, **kwargs):
        """Updates the specified values of the Square object.

        args:
            args: a tuple containing values for (id, size, x, y) in that order.
            kwargs: a dictionary of key/value pairs for the Square object.The
            order of the key/value pairs can be random.
        """
        if args and len(args) != 0:
            for item in range(len(args)):
                if item == 0:
                    self.id = args[item]
                elif item == 1:
                    self.size = args[item]
                elif item == 2:
                    self.x = args[item]
                elif item == 3:
                    self.y = args[item]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                elif key == "id":
                    self.id = value

    def to_dictionary(self):
        """Returns a dictionary representation of a Rectangle object"""
        return ({"id": self.id, "x": self.x, "size": self.size,
                 "y": self.y})
