#!/usr/bin/python3
"""Module that fetches a URL and displays X-Request-Id header using requests"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
