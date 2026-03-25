#!/usr/bin/python3
"""This module defines a is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or inherits from it"""
    return isinstance(obj, a_class)
