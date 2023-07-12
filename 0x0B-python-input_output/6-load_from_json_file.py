#!/usr/bin/python3

"""This module defines a function load_from_json_file(filename)

load_from_json_file(filename) creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file

    args:
        filename: JSON file to create an object from.
    Returns: the object created or Deserialized
    """
    with open(filename) as file:
        obj = json.load(file)
        return(obj)
