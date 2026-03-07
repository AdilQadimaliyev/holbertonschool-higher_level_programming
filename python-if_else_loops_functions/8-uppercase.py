#!/usr/bin/python3
def uppercase(str):
    result = ""
    for ch in str:
        if 97 <= ord(ch) <= 122:
            result += chr(ord(ch) - 32)
        else:
            result += ch
    print("{}".format(result))
