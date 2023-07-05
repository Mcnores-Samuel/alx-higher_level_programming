#!/usr/bin/python3

"""This module contains one function print_square(size)

print_square(size) Prints a square of length (size) with
the character #
for example:
>>> print_square(4)
####
####
####
####
>>> print_square(10)
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
"""


def print_square(size):
    """Prints a square with the character #

    args:
        size: the size length of the square
    Returns: None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for n in range(size):
        print("#" * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt", verbose=True)
