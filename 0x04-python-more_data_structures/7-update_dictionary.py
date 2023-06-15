#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary.

    args:
        a_dictionary: a dictionary to manipulate or update_dictionary
        key: a key to check if it exist or create it.
        value: a value to the key
    Returns: an updated dictionary
    """
    if a_dictionary and key and value:
        if isinstance(a_dictionary, dict):
            if key in a_dictionary:
                a_dictionary[key] = value
            else:
                a_dictionary[key] = value
        return a_dictionary
    else:
        a_dictionary[key] = value
        return a_dictionary
