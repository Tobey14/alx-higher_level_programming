#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = map(lambda x: x if x in set_1 else None, set_2)
    return (new_list)
