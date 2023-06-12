#!/usr/bin/python3


def max_integer(my_list=[]):
    """Finds the biggest integer of a list.

    args:
        my_list: a list of integer to look for the max value
    Returns: the maximun integer in the list
    """
    if isinstance(my_list, list):
        if len(my_list) == 0:
            return None
        else:
            max_num = 0
            for n in my_list:
                if n > max_num:
                    max_num = n
            return max_num
