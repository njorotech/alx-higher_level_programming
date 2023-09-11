#!/usr/bin/python3

""" A class that inherits from another class"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """a method that prints the list in a sorted asceding order"""

        print(sorted(self))
