#!/usr/bin/python3

"""This module contains one function say_my_name(first_name, last_name)

say_my_name function take two strings representing first name
and last name print the out.
for example:
>>>say_my_name("Samuel", "Mcnores")
My name is Samuel Mcnores
"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>

    args:
        first_name: user first name
        last_name: user last name
    Returns: None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt", verbose=True)
