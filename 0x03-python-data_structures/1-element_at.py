#!/usr/bin/python3
def element_at(my_list, idx):
    element = my_list[idx]
    if element < 0 or idx > len(my_list):
        return
    else:
        return element
