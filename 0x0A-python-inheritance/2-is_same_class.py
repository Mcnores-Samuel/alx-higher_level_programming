#!/usr/bin/python3

"""This module defines a function is_same_class(obj, a_class)

is_same_class(obj, a_class) Take an obj check if is an instance of a class.
    pass
"""


def is_same_class(obj, a_class):
    """Checks if obj is an instance of a class or not

    args:
        obj: an object to test if it is an instance of  a_class.
        a_class: a class a test against obj.
    Returns: True if obj is an instance of a_class or False otherwise.
    """
    if isinstance(obj, a_class) and type(obj) == a_class:
        return (True)
    else:
        return (False)


if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
