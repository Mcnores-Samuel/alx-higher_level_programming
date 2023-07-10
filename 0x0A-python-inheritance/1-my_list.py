#!/usr/bin/python3

"""This module defines a class MyList with one method
print_sorted(self).

Inherits from the list class and prints a sorted list
for example:
>>> my_list = MyList()
>>> my_list.append(1)
>>> my_list.append(4)
>>> my_list.append(2)
>>> my_list.append(3)
>>> my_list.append(5)
>>> print(my_list)
[1, 4, 2, 3, 5]
>>> my_list.print_sorted()
[1, 4, 2, 3, 5]
>>> print(my_list)
[1, 4, 2, 3, 5]
"""


class MyList(list):
    """define MyList class and Inherits from list class"""
    def print_sorted(self):
        """Prints a sorted list object"""
        print(sorted(self))


if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
