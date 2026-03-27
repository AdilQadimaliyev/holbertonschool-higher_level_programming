#!/usr/bin/python3
"""This module defines a Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that defines a rectangle"""

    def __init__(self, width, height):
        """Initializes a rectangle with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
