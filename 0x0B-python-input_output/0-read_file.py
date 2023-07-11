#!/usr/bin/python3

"""This module defines one function read_file(fileneme="")

read_file(fileneme="") reads data from a file in utf-8 and print
it to the console. The data is usually text in utf-8.
"""


def read_file(filename=""):
    """Read from a text file object and print out the text

    args:
        filename: The name of the file to read from.
    Returns: None.
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
