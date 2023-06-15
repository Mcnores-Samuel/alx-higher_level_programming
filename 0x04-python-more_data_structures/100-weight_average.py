#!/usr/bin/python3


def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple"""
    if not my_list:
        return 0
    else:
        overall_sum = 0
        weight_sum = 0
        for tuple_n in my_list:
            overall_sum += tuple_n[0] * tuple_n[1]
            weight_sum += tuple_n[1]
        return overall_sum / weight_sum
