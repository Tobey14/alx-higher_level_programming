#!/usr/bin/python3
"""defining a function read_file"""


def read_file(filename=""):
    """Reads a file using the with"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
