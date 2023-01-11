#!/usr/bin/python3
"""
Defines a function to_json_string
"""
import json

def to_json_string(my_obj):
    """returns the json representation of an object using the with"""
    return json.dumps(my_obj)
