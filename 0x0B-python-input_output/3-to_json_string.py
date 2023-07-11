#!/usr/bin/python3
import json

"""This module defines a function to_json_string(my_obj)

to_json_string(my_obj) returns the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)

    args:
        my_obj: an object to create its json representation.
    Returns: the JSON representation of an object (string)
    """
    return (json.dumps(my_obj))
