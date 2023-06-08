#!/usr/bin/python3

if __name__ == "__main__":
    """
    import the following function from calculator_1 module
    add : returns the sum of two numbers
    sub : returns the difference of two integers
    div : returns the division of two numbers
    mul : returns the product or two integer.
    """
    from calculator_1 import add, sub, div, mul

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
