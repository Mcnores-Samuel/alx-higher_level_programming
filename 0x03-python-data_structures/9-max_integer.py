#!/usr/bin/python3


def max_integer(my_list=[]):
    """Finds the biggest integer of a list.

    args:
        my_list: a list of integer to look for the max value
    Returns: the maximun integer in the list
    """
    if not my_list:
        return None
    else:
        max = 0
        for n in my_list:
            if n > max:
                max = n
        return max
