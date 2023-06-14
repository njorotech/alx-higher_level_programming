#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    length = len(my_list)
    if len(my_list) == 0:
        return 0
    for i in my_list:
        sum += i[1]
    return sum / length
