#!/usr/bin/python3
"""This module defines a class_to_json function"""


def class_to_json(obj):
    """Returns dictionary description for JSON serialization of an object"""
    return obj.__dict__
