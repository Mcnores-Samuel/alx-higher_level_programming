#!/usr/bin/python3

"""This module define Base class for all subclasses"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        args:
            list_dictionaries: a list of dictionaries
        Returns: JSON string representation.
        """
        str_data = "[]"
        if list_dictionaries:
            str_data = json.dumps(list_dictionaries)
        return(str_data)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        args:
            list_objs: is a list of instances who inherits of Base
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_data = [item.to_dictionary() for item in list_objs]
                data = Base.to_json_string(list_data)
                file.write(data)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string

        args:
            json_string:  a string representing a list of dictionaries
        Returns: the list represented by json_string
        """
        if json_string is None:
            return []
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        args:
            dictionary: can be thought of as a double pointer to a dictionary
        Returns; an instance of Base subclasses.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                temp_obj = cls(10, 10)
            else:
                temp_obj = cls(1)
            temp_obj.update(**dictionary)
            return (temp_obj)

    @classmethod
    def load_from_file(cls):
        """Creates a list of instances from json file"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                js_string = file.read()
                data_list = Base.from_json_string(js_string)
                instance_list = [cls.create(**item) for item in data_list]
                return instance_list
        except (FileExistsError, FileNotFoundError, IOError):
            return []
