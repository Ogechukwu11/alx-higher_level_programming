#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
