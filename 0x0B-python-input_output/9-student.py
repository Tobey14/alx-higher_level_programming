#!/usr/bin/python3
"""Defines a class Student
"""

class Student:
    """student class with public attributes first_name last_name age and a public method to_json"""

    def __init__(self, first_name, last_name, age):
        """initialize the class with public values first_name last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns the dictionary description for the class
        """
        return self.__dict__
