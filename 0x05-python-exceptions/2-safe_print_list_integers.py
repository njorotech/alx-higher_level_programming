#!/bin/usr/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    k = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            k += 1
        except Exception:
            pass
        i += 1
    print()
    return k
