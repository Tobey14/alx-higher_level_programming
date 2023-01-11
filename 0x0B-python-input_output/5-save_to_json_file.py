#!/usr/bin/python3
"""
Defines a function save_to_json_string
"""
import json

def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation
    """
    with open(filename, "w") as f:
        return (json.dump(my_obj, f))
