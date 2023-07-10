#!/usr/bin/python3

"""This module defines a function is_kind_of_class(obj, a_class)

is_kind_of_class(obj, a_class) Take an obj check if is an instance of a class.
    pass
"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a class or
    if the object is an instance of a class that inherited from,

    args:
        obj: an object to test if it is an instance of  a_class.
        a_class: a class a test against obj.
    Returns: True if obj is an instance of a_class or False otherwise.
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)


if __name__ == "__main__":
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
