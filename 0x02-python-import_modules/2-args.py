#!/usr/bin/python3

if __name__ == "__main_":
    """takes command line arguments"""
    import sys

    arg_arr = sys.argv
    size = len(arg_arr)

    if size == 1:
        print("{} arguments.".format(size - 1))
    elif size == 2:
        print("{} argument:".format(size - 1))
        print("{}: {}".format(size - 1, arg_arr[size - 1]))
    else:
        print("{} arguments:".format(size - 1))
        for n in range(1, size):
            print("{}: {}".format(n, arg_arr[n]))
