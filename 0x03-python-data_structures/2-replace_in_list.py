#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position.

    args:
        my_list: a list to modify.
        idx: integer denoting position of an element.
        element: a new element to add at specified position.
    Returns: a modified list with value at position idx or original list
            if not modified
    """
    if idx < 0 or idx > len(my_list) - 1:
        pass
    else:
        my_list[idx] = element

    return my_list
