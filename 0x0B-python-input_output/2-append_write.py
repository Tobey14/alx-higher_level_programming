#!/usr/bin/python3
"""
append a string to a text file (UTF8) and returns
the number of characters written:

Prototype: def append_write(filename="", text=""):
Appends to the file.
"""

def append_write(filename="", text=""):
    """appends to a file using the with"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
