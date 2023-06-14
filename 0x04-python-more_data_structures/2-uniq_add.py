#!/usr/bin/python3


def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer).

    args:
        my_list: a list to look for unique integers
    Returns: sum of all integers occur once in a list.
    """
    if not my_list:
        return 0
    else:
        if isinstance(my_list, list):
            new_list = set(my_list)
            new_list = list(new_list)
            sum_all = 0
            for n in new_list:
                sum_all += n
            return sum_all
