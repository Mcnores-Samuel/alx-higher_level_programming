#!/usr/bin/python3

if __name__ == "__main__":
    """import the following function from calculator_1 module
    add : returns the sum of two numbers 10 and 5
    sub : returns the difference of two integers 10 and 5
    div : returns the division of two numbers 10 and 5
    mul : returns the product or two integer 10 and 5
    """
    from calculator_1 import add, sub, div, mul

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
