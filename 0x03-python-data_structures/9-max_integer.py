#!/usr/bin/python3
def max_integer(my_list=[]):
    list_length = len(my_list)
    if list_length == 0:
        return None
    my_list.sort()
    return my_list[list_length - 1]
