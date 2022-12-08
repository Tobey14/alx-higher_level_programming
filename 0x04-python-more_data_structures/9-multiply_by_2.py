#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_list = dict(map(lambda x: x * 2, a_dictionary))
    return (new_list)
