#!/usr/bin/python3

"""This module has one function lookup(obj).

lookup(obj) return a list of available list and attributes of an object.
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object

    args:
        obj(object): an object to list all its attributesa and methods.
    Returns: the list of available attributes and methods of an object
    """
    return (dir(obj))


if __name__ == "__main__":
    class Myclass:
        pass

    print(lookup(int))
