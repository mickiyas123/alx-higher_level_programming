#!/usr/bin/python3
"""Unitest for max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInt(unittest.TestCase):
    """TestCase for the max_integer function."""
    def test_max(self):
        # Test the max value of an int
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 3, 5, 4, 2]), 5)
        self.assertAlmostEqual(max_integer([4, 3, 4, 1]), 4)
        self.assertAlmostEqual(max_integer([-4, -3, -4, -1]), -1)
        self.assertAlmostEqual(max_integer([-4, 3, 4, 1]), 4)
