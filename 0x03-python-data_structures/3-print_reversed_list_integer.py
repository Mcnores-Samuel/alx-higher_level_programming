#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list, in reverse order.

    args:
        my_list: a list to reverse
    Returns: nothing
    """
    for n in range(1, len(my_list)):
        n = n * -1
        print("{:d}".format(my_list[n]))
