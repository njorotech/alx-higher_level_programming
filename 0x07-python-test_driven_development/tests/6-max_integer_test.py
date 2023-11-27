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
        self.assertEqual(max_integer([6, 1, 2, 3, 5]), 6)
        self.assertEqual(max_integer([1, 2, 7, 3, 5]), 7)
        self.assertEqual(max_integer([1, 2, -3, 5]), 5)
        self.assertEqual(max_integer([-1, -2, -3, -5]), -1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
