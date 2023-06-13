#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list.

    args:
        my_list: a list to find multiples on.
    Returns: a new list containing boolean values
    """
    if isinstance(my_list, list):
        if my_list:
            new_list = []
            for n in my_list:
                if n % 2 == 0:
                    new_list.append(True)
                else:
                    new_list.append(False)
            return new_list
