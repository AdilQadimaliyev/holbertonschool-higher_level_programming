#!/usr/bin/python3
"""This module defines a to_json_string function"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object"""
    return json.dumps(my_obj)
