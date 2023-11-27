#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TextMaxInteger(unittest.TestCase):
    """Class to test max_integer function"""

    def test_max_integer(self):
        """function to test max_integer funtion"""

        self.assertEqual(max_integer([1, 2, 3, 5]), 5)
