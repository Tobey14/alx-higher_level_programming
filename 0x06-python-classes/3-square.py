#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """

    def __init__(self, size=0):
        """Initializes a square
        Args:
            size (int): size of a side of the square
        Returns: None
        """

        if(type(size) is not int):
            """
            Raise TypeError if size isn't integer
            """
            raise TypeError('size must be an integer')
        
        if(size < 0):
            """
            Raise ValueError if size is less than zero
            """
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2
