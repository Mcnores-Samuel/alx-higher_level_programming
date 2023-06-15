#!/usr/bin/python3


def roman_to_int(roman_string):
    """converts a Roman numeral to an integer"""
    roman_numeral = {
        "M": 1000, "D": 500,
        "C": 100, "L": 50,
        "X": 10, "V": 5, "I": 1
    }

    result = 0

    if not roman_string:
        return result
    else:
        for i in roman_string:
            if i in roman_numeral:
                result += roman_numeral[i]
        return result
