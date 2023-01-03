#!/usr/bin/python3
"""Defines a module that add two integers or floats a and b"""

def add_integer(a, b=98):
    """adds two integers or floats
    Args:
        value (a, b): integers to be added
    Returns:
        the sum of both integers
    """
    if type(a) is not int or type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        sum = int(a) + int(b)
        return sum
