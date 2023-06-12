#!/usr/bin/python3


def no_c(my_string):
    """Removes all characters c and C from a string.

    args:
        my_string: a string literal to removes c or C from.
    Returns: a new string without c or C characters.
    """
    if my_string:
        result_str = ""
        for char in my_string:
            if char != "c" and char != "C":
                result_str += char
        return result_str
    else:
        pass
