#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list.

    args:
        my_list: a list containing any type (integer, string, etc).
        x: represents number of elements to print.
    Return: The real number of elements printed.
    """
    i = 0
    try:
        if my_list and isinstance(my_list, list):
            for n in range(x):
                i += 1
                print("{}".format(my_list[n]), end="")
    except IndexError:
        pass
    return (i)
