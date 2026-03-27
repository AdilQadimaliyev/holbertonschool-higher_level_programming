#!/usr/bin/python3
"""This module defines a CustomObject class with pickle serialization"""
import pickle


class CustomObject:
    """A custom class that can be serialized and deserialized"""

    def __init__(self, name, age, is_student):
        """Initializes a CustomObject"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object's attributes"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serializes the current instance and saves it to a file"""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Loads and returns an instance of CustomObject from a file"""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
