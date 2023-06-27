#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list.

    args:
        my_list: a list containing any type (integer, string, etc).
        x: represents number of elements to print.
    Returns: The real number of elements printed.
    """
    i = 0
    if my_list and isinstance(my_list, list):
        for n in range(x):
            try:
                print("{}".format(my_list[n]), end="")
                i += 1
            except IndexError:
                break
    print()
    return (i)
