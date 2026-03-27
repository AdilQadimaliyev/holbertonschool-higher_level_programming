#!/usr/bin/python3
"""This module defines basic serialization functions"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python dictionary and saves it to a JSON file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Loads and deserializes data from a JSON file"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
