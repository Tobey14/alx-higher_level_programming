#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numerator = 0
    denominator = 0

    for index in my_list:
        numerator += index[0] * index[1]
        denominator += index[1]

    return (numerator / denominator)
