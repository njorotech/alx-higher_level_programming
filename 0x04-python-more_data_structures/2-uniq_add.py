#!/usr/bin/python3
def uniq_add(my_list=[]):
    sam = 0
    uniq_list = set(my_list)
    for i in uniq_list:
        sam += i
    return sam

