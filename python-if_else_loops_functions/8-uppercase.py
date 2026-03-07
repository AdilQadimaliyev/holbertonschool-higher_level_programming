#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        o = ord(ch)
        if 97 <= o <= 122:
            print("{}".format(chr(o - 32)), end="")
        else:
            print("{}".format(ch), end="")
    print("")
