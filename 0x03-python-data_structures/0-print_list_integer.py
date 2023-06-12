#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """Prints all integers of a list

    args:
        my_list: list of integers
    """
    for n in my_list:
        print("{:d}".format(n))
