#!/usr/bin/python3


def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    max_value = 0
    result = ""
    if a_dictionary and isinstance(a_dictionary, dict):
        for key, value in a_dictionary.items():
            if value > max_value:
                max_value = value
                result = key
        return result
