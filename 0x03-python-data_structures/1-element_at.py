#!/usr/bin/python3


def element_at(my_list, idx):
    """Retrieves an element from a list at index.

    args:
        my_list: a list to retrieves an item from.
        idx: an integers denoting index of an element in the list.
    Returns: an element at position idx or  None.
    """
    if idx < 0 or idx > len(my_list) - 1:
        return None
    else:
        return my_list[idx]
