#!/usr/bin/python3

"""This module defines a function save_to_json_file(my_obj, filename)

save_to_json_file(my_obj, filename) writes an Object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ Writes an Object to a text file,
    using a JSON representation

    args:
        my_obj: an object to it's json representation to a text file.
        filename: a file to write a json representation of my_obj object.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
