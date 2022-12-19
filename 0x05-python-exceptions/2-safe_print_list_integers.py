#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            if(type(my_list[i]) is int):
                print(my_list[i], end='')
                count += 1
        print(' ')
        return count
    except IndexError:
        print('IndexError: list index out of range')
