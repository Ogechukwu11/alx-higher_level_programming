#!/usr/bin/python3
for character in range(97, 123):
    if chr(character) == 'q' or chr(character) == 'e':
        continue
    print("{}".format(chr(character)), end="")
