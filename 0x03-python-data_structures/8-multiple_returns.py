#!/usr/bin/python3


def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character.

    args:
        sentence: a string to calculate its length and its first character.
    Returns: a tuple with the length of a string and its first character.
    """
    if sentence:
        result = [len(sentence), sentence[0]]
        result = tuple(result)
        return result
