#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list, in reverse order.

    args:
        my_list: a list to reverse
    Returns: nothing
    """
    my_list = my_list.reverse()
    for n in my_list:
        print("{:d}".format(my_list[n]))
