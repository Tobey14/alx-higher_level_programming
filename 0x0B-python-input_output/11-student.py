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

    def to_json(self, attrs=None):
        """
        Returns the dictionary description for the class
        """
        if attrs == None or type(attrs) != list:
            return self.__dict__
        else:
            temp = {}
            for elem in attrs:
                if type(elem) != str:
                    return self.__dict__
                if elem in self.__dict__.keys():
                    temp[elem] = self.__dict__[elem]
            return temp
        
    def reload_from_json(self, json):
        """Replaces all items in `json`
        """

        for items in json.keys():
            self.__dict__[items] = json[items]
        