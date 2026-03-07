#!/usr/bin/python3
def uppercase(str):
result = ""
for ch in str:
o = ord(ch)
if 97 <= o <= 122:
result += chr(o - 32)
else:
result += ch
print("{}".format(result))
