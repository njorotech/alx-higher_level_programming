#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    j = 1
    i = 0
    while i <= j:
        if tuple_a[i] is None:
            tuple_a[i] = 0
        if tuple_b[i] is None:
            tuple_b[i] = 0
        new_tuple = tuple_a[i] + tuple_b[i]
        i += 1
