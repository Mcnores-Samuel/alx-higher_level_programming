#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list.

    args:
        my_list: a list to search and create a copy of the modified list.
        search: an element to search for in a list.
        replace: element to replace the searched element.
    Returns: a new modified list with search elements replaced.
    """
    if isinstance(my_list, list) and my_list:
        new_list = [n for n in my_list]
        for n in range(len(new_list)):
            if new_list[n] == search:
                new_list[n] = replace
        return new_list
