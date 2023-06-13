#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i >= 'a' and i <= 'z':
            asc = ord(i) - 32
            print("{}".format(chr(asc)), end="")
        else:
            print("{}".format(i), end="")
    print()
