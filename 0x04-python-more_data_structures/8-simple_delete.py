#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary."""
    if a_dictionary and key in a_dictionary:
        del a_dictionary[key]
        return a_dictionary
    else:
        return a_dictionary
