#!/usr/bin/python3
"""This module defines a write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns number of characters"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
