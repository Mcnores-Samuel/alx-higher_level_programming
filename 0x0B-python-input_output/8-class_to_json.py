#!/usr/bin/python3

"""This module defines a class_to_json(obj) function"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    return (obj.__dict__)
