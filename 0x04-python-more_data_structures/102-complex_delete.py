#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary."""
    if a_dictionary and value:
        new_dict = {}
        for key, v, in a_dictionary.items():
            if v != value:
                new_dict[key] = v
        a_dictionary = new_dict
        return new_dict
    else:
        return a_dictionary
