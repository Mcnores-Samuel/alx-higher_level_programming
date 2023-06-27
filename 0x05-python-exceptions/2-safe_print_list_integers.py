#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers.

    args:
        my_list: a list can contain any type (integer, string, etc.)
        x(int): represents the number of elements to access in my_list.
    Returns: The real number of integers printed.
    """
    items = 0
    for n in range(x):
        try:
            print("{:d}".format(my_list[n]), end="")
            items += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
    print()
    return (items)
