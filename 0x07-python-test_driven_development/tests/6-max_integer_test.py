#!/usr/bin/python3
"""Module to test the function def max_integer(list=[]):"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class test_max_integer(unittest.TestCase):
    """Class to test max_integer function"""

    def test_max_integer(self):
        """function to test max_integer funtion"""

        self.assertEqual(max_integer([1, 2, 3, 5]), 5)
