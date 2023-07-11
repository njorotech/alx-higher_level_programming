#!/usr/bin/python3

'''Reads UTF8'''


def read_file(filename=""):
    '''reads a text file and prints it to stdout'''

    with open(filename, encoding='utf-8') as myfile:
        for line in myfile:
            print(line, end='')
