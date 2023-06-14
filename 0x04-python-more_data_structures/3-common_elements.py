#!/usr/bin/python3


def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets.
    """
    if set_1 and set_2:
        return set_1 & set_2
    else:
        return set()
