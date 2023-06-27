#!/usr/bin/python3


def safe_print_division(a, b):
    """Divides 2 integers and prints the result.

    args:
        a: first integer
        b: second integer
    Returns: result of the division of a and b or None otherwise.
    """
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return (result)
