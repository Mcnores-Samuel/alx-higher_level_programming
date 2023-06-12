#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position
       without modifying the original list.

    args:
        my_list:  original list to make a copy from.
        idx: index position to modify a value in a copy of the list.
        element: item to add at position idx
    Returns: modified copy of the original list or unmodified copy.
    """
    if isinstance(my_list, list) and my_list:
        copy_list = [n for n in my_list]

        if idx < 0:
            return copy_list
        elif idx > len(my_list) - 1:
            return copy_list
        else:
            copy_list[idx] = element
        return copy_list
