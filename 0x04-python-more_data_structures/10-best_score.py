#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    
    sorted = a_dictionary.sort()
    return (sorted[-1])
