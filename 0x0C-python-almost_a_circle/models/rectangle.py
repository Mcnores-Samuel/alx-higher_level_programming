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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves the width of the Rectangle object"""
        return (self.__width)

    @width.setter
    def width(self, width):
        """Sets the width of the Rectangle object

        args:
            width: must be an integer
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Retrieves the height of the Rectangle object"""
        return (self.__heigth)

    @height.setter
    def height(self, height):
        """Sets the height value to the Rectangle object

        args:
           height: must be an integer
        """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__heigth = height

    @property
    def x(self):
        """Retrieves the value of x"""
        return (self.__x)

    @x.setter
    def x(self, x):
        """Sets the value if x(int value)

        args:
           x: must be an integer
        """
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Retrieves the value of y"""
        return (self.__y)

    @y.setter
    def y(self, y):
        """Sets the value of y(int value)

        args:
            y: must be an integer
        """
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of the Rectangle object"""
        return (self.__width * self.__heigth)

    def display(self):
        """print the Rectangle object using character #"""
        [print("") for n in range(self.__y)]
        for i in range(0, self.__heigth):
            [print(" ", end="") for n in range(self.__x)]
            [print("#", end="") for n in range(self.__width)]
            print()

    def __str__(self):
        """String representation of the Rectangle object"""
        result = "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                  self.id, self.__x, self.__y,
                                                  self.__width, self.__heigth)
        return (result)

    def update(self, *args, **kwargs):
        """Updates the specified values of the Rectangle object"""
        if args and len(args) != 0:
            for item in range(len(args)):
                if item == 0:
                    self.id = args[item]
                elif item == 1:
                    self.width = args[item]
                elif item == 2:
                    self.height = args[item]
                elif item == 3:
                    self.x = args[item]
                elif item == 4:
                    self.y = args[item]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                elif key == "id":
                    self.id = value

    def to_dictionary(self):
        """Returns a dictionary representation of a Rectangle object"""
        return ({"x": self.x, "y": self.y, "id": self.id,
                 "height": self.height, "width": self.width})
