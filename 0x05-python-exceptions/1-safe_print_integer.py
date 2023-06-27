#!/usr/bin/python3


def safe_print_integer(value):
    """Prints an integer if a value is an integer.

    args:
        value: (int) value to print.
    Returns: True if value is an integer or False if not.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
