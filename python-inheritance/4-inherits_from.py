#!/usr/bin/python3
"""This module defines a inherits_from function"""


def inherits_from(obj, a_class):
    """Returns True if obj is instance of a class that inherited a_class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
