#!/usr/bin/python3
"""This module defines a convert_csv_to_json function"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts CSV data to JSON format and writes it to data.json"""
    try:
        with open(csv_filename, encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)
        return True
    except FileNotFoundError:
        return False
