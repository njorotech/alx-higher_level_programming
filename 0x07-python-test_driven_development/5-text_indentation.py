#!/usr/bin/python3
"""Text indentation module"""


def text_indentation(text):
    """
    A function that prints a text with 2
    new lines after each these characters: ., ?, and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

