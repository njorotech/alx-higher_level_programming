#!/usr/bin/python3

'''Write to file'''


def write_file(filename="", text=""):
    ''' writes a string to a text file'''

    with open(filename, mode='w', encoding='utf-8') as myfile:
        characters = myfile.write(text)
    return characters
