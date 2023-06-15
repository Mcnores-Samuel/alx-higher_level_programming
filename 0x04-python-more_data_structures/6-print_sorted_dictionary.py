#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys.
    """
    if a_dictionary and isinstance(a_dictionary, dict):
        for key, value in sorted(a_dictionary.items()):
            print("{}: {}".format(key, value))
