#!/usr/bin/python3

"""This module defines a function inherits_from(obj, a_class)

inherits_from(obj, a_class) Take an obj check if is an instance of a class.
    pass
"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    args:
        obj: an object to test if it inherits from  a_class.
        a_class: a class a test against obj.
    Returns: True if obj inherits from a_class or False otherwise.
    """
    if issubclass(type(obj), a_class) and a_class != type(obj):
        return (True)
    else:
        return (False)


if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
