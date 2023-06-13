#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list.

    args:
        my_list: a list to delete a value from.
        idx: index position at which a value is to be deleted.
    Returns: a new list without the deleted value
    """
    if isinstance(my_list, list):
        if not my_list and idx == 0:
            return []
        if my_list:
            if idx < 0 or idx > len(my_list) - 1:
                return my_list
            else:
                del my_list[idx]
                return my_list
