#!/usr/bin/python3
"""
This module contains a test for the class Base for the save_to_file method,
which involves the classes Rectangle and Square.
"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBaseSaveToFile(unittest.TestCase):
    """
    This is the class that tests the save_to_file method.
    """


def test_save_empty_list(self):
    """
    This method tests for an empty list.
    """


Square.save_to_file([])
with open("Square.json", "r") as f:
    self.assertEqual("[]", f.read())


def test_save_one_rectangle(self):
    """
    This method tests for one rectangle.
    """
    r1 = Rectangle(10, 7, 2, 8)
    Rectangle.save_to_file([r1])
    with open("Rectangle.json", "r") as f:
        self.assertEqual(
            '[{"id": 18, "x": 2, "y": 8, "width": 10, "height": 7}]', f.read()
        )


def test_save_one_square(self):
    """
    This method tests for one square.
    """
    s1 = Square(10, 7, 2, 8)
    Square.save_to_file([s1])
    with open("Square.json", "r") as f:
        self.assertEqual('[{"id": 8, "x": 7, "y": 2, "size": 10}]', f.read())


def test_save_overwrite(self):
    """
    This method tests for overwrite.
    """
    s1 = Square(10, 2, 1, 1)
    Square.save_to_file([s1])
    s2 = Square(1, 1)
    Square.save_to_file([s2])
    with open("Square.json", "r") as f:
        self.assertEqual('[{"id": 19, "x": 1, "y": 0, "size": 1}]', f.read())


def test_save_no_args(self):
    """
    This method tests for zero arguments.
    """
    with self.assertRaises(TypeError):
        Square.save_to_file()


def test_save_two_arg(self):
    """
    This method tests for more than one argument.
    """
    with self.assertRaises(TypeError):
        Rectangle.save_to_file([], [])
