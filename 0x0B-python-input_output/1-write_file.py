#!/usr/bin/python3

"""This module defines a function write_file(filename="", text="")

write_file(filename="", text="") write text to the file by overwriting the
current text in the file with the new text.
"""


def write_file(filename="", text=""):
    """Write text to a text file or overwrites a file.

    args:
        filename: a file to write to.
        text: the new text to write to the file.
    Returns: number of characters written.
    """
    written = 0
    with open(filename, "w", encoding="utf-8") as file:
        written = file.write(text)
    return (written)
