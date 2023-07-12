#!/usr/bin/python3

"""This module defines a Student class"""


class Student:
    """defines a student class"""
    def __init__(self, first_name, last_name, age):
        """Initializes Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=[]):
        """retrieves a dictionary representation of a Student instance
        args:
           attrs: is a list of strings, only attribute names contained
           in this list must be retrieved.
        """
        if type(attrs) == list and all(type(item) == str
                                       for item in attrs):
            return ({key: getattr(self, key) for
                     key in attrs if hasattr(self, key)})
        return (self.__dict__)

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

        args:
            json: a dictionary
        """
        for key, value in json.items():
            if key == "first_name":
                self.first_name = value
            elif key == "last_name":
                self.last_name = value
            else:
                self.age = value
