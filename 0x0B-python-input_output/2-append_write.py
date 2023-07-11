#!/usr/bin/python3

"""This module defines a function append_write(filename="", text="")

append_write(filename="", text="") append or adds text at the end of the file.
"""


def append_write(filename="", text=""):
    """Append a text at the end of the file.

    args:
        filename: a file to write to.
        text: the new text to write to the file.
    Returns: number of characters written.
    """
    written = 0
    with open(filename, "w", encoding="utf-8") as file:
        written = file.write(text)
    return (written)
