#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2"""
    new_dict = {}
    if a_dictionary:
        for key, value in a_dictionary.items():
            new_dict[key] = value * 2
        return new_dict
