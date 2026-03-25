#!/usr/bin/python3
"""This module defines a Square class"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        """Initializes a square with optional size"""
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
