#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = list(sys.argv)
    size = len(args) - 1

    sum = 0
    for n in range(1, size + 1):
        if not isinstance(int(args[n]), int):
            sum += 0
            continue
        else:
            sum += int(args[n])
    print("{}".format(sum))
