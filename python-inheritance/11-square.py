#!/usr/bin/python3
"""This module defines a Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that defines a square"""

    def __init__(self, size):
        """Initializes a square with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
