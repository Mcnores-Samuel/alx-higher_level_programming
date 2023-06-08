#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = list(sys.argv)
    length = len(args) - 1

    if length == 0:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
        print("{}: {}".format(length, args[length]))
    else:
        print("{} arguments:".format(length))
        for n in range(1, length + 1):
            print("{}: {}".format(n, args[n]))
