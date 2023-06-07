#!/usr/bin/python3

def uppercase(str):
    i = 0
    result = ""
    while i < len(str):
        if ord(str[i]) >= 97 and ord(str[i]) < 123:
            char = (ord(str[i]) - 97) + 65
            result += chr(char)
        else:
            result += str[i]
        i += 1
    print("{:s}".format(result))
