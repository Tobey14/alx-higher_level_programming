#!/usr/bin/python3
"""
Defines a function to_json_string
"""
import json

def from_json_string(my_str):
    """returns the json representation of an object using the with"""
    return json.load(my_str)
