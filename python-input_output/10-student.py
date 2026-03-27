#!/usr/bin/python3
"""This module defines a Student class"""


class Student:
    """A class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student"""
        if isinstance(attrs, list):
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__
