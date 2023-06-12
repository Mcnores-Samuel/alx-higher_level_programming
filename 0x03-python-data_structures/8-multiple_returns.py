#!/usr/bin/python3


def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character.

    args:
        sentence: a string to calculate its length and its first character.
    Returns: a tuple with the length of a string and its first character.
    """
    char = ""
    if sentence:
        char = sentence[0]
    else:
        char = None
    result = [len(sentence), char]
    result = tuple(result)
    return result
