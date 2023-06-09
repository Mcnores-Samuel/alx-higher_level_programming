#!/usr/bin/python3

if __name__ == "__main__":
    """calculate two, by addition, subtract, multiply and division"""
    from calculator_1 import add, sub, mul, div
    import sys

    args = list(sys.argv)
    arg_count = len(args) - 1

    if arg_count < 3:
        print("Usage: {} <a> <operator> <b>".format(args[0]))
        sys.exit(1)

    a = int(args[1])
    b = int(args[arg_count])
    op_dict = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    if args[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    for key, value in op_dict.items():
        if key == args[2]:
            print("{} {} {} = {}".format(a, key, b, value(a, b)))
