#!/usr/bin/python3


def roman_to_int(roman_string):
    """converts a Roman numeral to an integer"""
    roman_numeral = {
        "M": 1000, "D": 500,
        "C": 100, "L": 50,
        "X": 10, "V": 5, "I": 1
    }

    result_list = []
    total_sum = 0

    if not roman_string or roman_string is None:
        return total_sum
    else:
        for i in roman_string:
            if i in roman_numeral:
                result_list.append(roman_numeral[i])

        for n in range(len(result_list)):
            try:
                if result_list[n] < result_list[n + 1]:
                    total_sum -= result_list[n]
                else:
                    total_sum += result_list[n]
            except IndexError:
                total_sum += result_list[n]
        return total_sum
