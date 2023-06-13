#!/usr/bin/python3
asc = 97
while asc < 123:
    if asc != 113 and asc != 101:
        print("{}".format(chr(asc)), end="")
    asc += 1
