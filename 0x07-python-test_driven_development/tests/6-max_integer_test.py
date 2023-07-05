#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([5, 8, 25, 24, 23]), 25)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([]), None)
        self.assertRaises(TypeError, max_integer, [1, 2, 'a', 4])
        