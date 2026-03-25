#!/usr/bin/python3
"""This module defines a Square class"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        """Initializes a square with optional size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
