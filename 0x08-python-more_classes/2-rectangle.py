#!/usr/bin/python3
"""Defines a class Rectangle"""

class Rectangle:
    """Represents a Rectangle
    Attributes:
        __width (int): width of the Rectangle 
        __height (int): height of the Rectangle
    """
    def __init__(self, width=0, height=0):
        """initializes the Rectangle
        Args:
            width (int): width of the Rectangle
            __height (int): height of the Rectangle
        Returns:
            None
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter of __width
        Returns:
            The width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter of __width
        Args:
            value (int): width of the Rectangle
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
    
    @property
    def height(self):
        """getter of __height
        Returns:
            The height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter of __height
        Args:
            value (int): height of the Rectangle
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

    def area(self):
        """Returns the area of rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__height + self.__width))
