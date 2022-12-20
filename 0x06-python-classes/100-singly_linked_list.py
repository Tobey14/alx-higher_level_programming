#!/usr/bin/python3
"""Defines a two classes Node and SinglyLinkedList"""


class Node:
    """Represents a Node Class
    Attributes:
        __data (int): data in a node
    """
    def __init__(self, data, next_node=None):
        """initializes the node
        Args:
            data (int): data of the node
        Returns:
            None
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """getter for the node class data"""
        return self.__data
    
    @data.setter
    def data(self, value): 
        """setter for the node class data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """getter for the node class next_node"""
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value): 
        """setter for the node class next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """Represents a single linked list Class
    Attributes:
        __head (int): head in a node
    """
    def __init__(self, head=None):
        """initializes the single linked list
        Args:
            head (int): head of the linked list
        Returns:
            None
        """
        self.__head = head
    
    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in the list"""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node

            new.next_node = tmp.next_node
            tmp.next_node = new
    
    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
