#!/usr/bin/python3

"""This module defines one function for adding integers

add_integer: adds two integers passed to it or return 98 as a
defualt value. for example:

>>>add_integer(10, 20)
30
>>>add_integer(2)
100
>>>add_integer(23)
121

That is if one value passed then the defualt value will be used for the second
argument.
"""


def add_integer(a, b=98):
    """Adds two integers and return their sum.

    args:
        a: first integer
        b: second integer
    Returns: an integer: the addition of a and b
    """
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")
    return (a + b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt",
                     globs={"add_integer": add_integer},
                     verbose=True)
