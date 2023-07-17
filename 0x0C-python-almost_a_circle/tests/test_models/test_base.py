#!/usr/bin/python3
'''
this module contains tests for the
load_from_file method of the
Base class
'''
from re import M, S
import unittest
import os
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class Test_Load_From_File(unittest.TestCase):
    '''
    tests for load_from_file of base.py
    '''

    def test_load_empty_file(self):
        '''
        empty file test
        '''
        if (os.path.exists("Rectangle.json") is True):
            os.remove("Rectangle.json")
        if (os.path.exists("Square.json") is True):
            os.remove("Square.json")
        if (os.path.exists("Base.json") is True):
            os.remove("Base.json")
        sq1 = Square.load_from_file()
        self.assertEqual(sq1, [])
        os.mknod("Rectangle.json")
        rect1 = Rectangle.load_from_file()
        self.assertEqual(rect1, [])

    def test_load_rectangle(self):
        '''
        Test for rectangles
        '''
        rect2 = Rectangle(10, 7, 2, 8)
        rect3 = Rectangle(2, 4)
        my_list = [rect2, rect3]
        Rectangle.save_to_file(my_list)
        my_list_loaded = Rectangle.load_from_file()
        self.assertEqual(type(my_list), type(my_list_loaded))
        self.assertEqual(len(my_list), len(my_list_loaded))
        for i in range(len(my_list)):
            self.assertEqual(my_list_loaded[i].to_dictionary(),
                             my_list[i].to_dictionary())
        os.remove("Rectangle.json")

    def test_load_square(self):
        '''
        Test for squares
        '''
        sq2 = Square(5)
        sq3 = Square(7, 9, 1)
        my_list = [sq2, sq3]
        Square.save_to_file(my_list)
        my_list_loaded = Square.load_from_file()
        self.assertEqual(type(my_list), type(my_list_loaded))
        self.assertEqual(len(my_list), len(my_list_loaded))
        for i in range(len(my_list)):
            self.assertEqual(my_list_loaded[i].to_dictionary(),
                             my_list[i].to_dictionary())
        os.remove("Square.json")

    def test_extra_args(self):
        '''
        Test for more arguments than is possible
        '''
        with self.assertRaises(TypeError):
            Base.load_from_file(Square)
