#!/usr/bin/python3

n = 122
set = False
while n >= 97:
    num = n
    if set:
        num = n - 97 + 65
        set = False
    else:
        set = True
    print("{:s}".format(chr(num)), end="")
    n -= 1
