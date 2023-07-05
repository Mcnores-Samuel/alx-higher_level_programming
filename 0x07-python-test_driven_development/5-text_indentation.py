#!/usr/bin/python3

"""This module contains a function text_indentation(text)
"""


def text_indentation(text):
    """ prints a text with 2 new lines after each of
    these characters: ., ? and :

    args:
        text: must be a string
    Returns: None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    n = 0
    while n < len(text):
        print(text[n], end="")
        if text[n] == "." or text[n] == "?" or text[n] == ":":
            try:
                if text[n + 1] == " ":
                    n += 1
            except IndexError:
                pass
            print("\n")
        n += 1
