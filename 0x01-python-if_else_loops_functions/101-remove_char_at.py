#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    counter = 0
    while counter < len(str):
        if counter != n:
            s += str[counter]
        counter += 1
    return s
