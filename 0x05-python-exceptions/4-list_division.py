#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists.

    args:
        my_list_1: first list can contain any type (integer, string, etc.)
        my_list_2: second list can contain any type (integer, string, etc.)
        list_length: integer representing length of both lists.
    Returns: a new list (length = list_length) with all divisions.
    """
    result_list = []
    num = 0
    for n in range(list_length):
        try:
            num = my_list_1[n] / my_list_2[n]
        except (ValueError, TypeError):
            num = 0
            print("wrong type")
        except ZeroDivisionError:
            num = 0
            print("division by 0")
        except IndexError:
            print("out of range")
            num = 0
        finally:
            result_list.append(num)
    return (result_list)
