#!/usr/bin/python3


def number_keys(a_dictionary):
    """Returns the number of keys in a dictionary"""
    if isinstance(a_dictionary, dict) and a_dictionary:
        key_count = 0
        for key in a_dictionary:
            key_count += 1
        return key_count
    else:
        return 0
