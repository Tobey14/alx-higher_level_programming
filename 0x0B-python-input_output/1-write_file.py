#!/usr/bin/python3
"""
Writes a string to a text file (UTF8) and returns
the number of characters written:

Prototype: def write_file(filename="", text=""):
Create the file if doesn’t exist and overwrite the content
of the file if it already exists.
"""

def write_file(filename="", text=""):
    """writes to a file using the with"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
