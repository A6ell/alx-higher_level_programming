#!/usr/bin/python3
'''
this module contains a test for the class Base
for the method save to file which
involves the class Rectangle and square
'''
import unittest
from models.base_abel import Base
from models.square_abel import Square
from models.rectangle_abel import Rectangle


class TestBase_save_to_file(unittest.TestCase):
    '''
    this is the class that tests the save to file method
    '''
    def test_save_empty_list(self):
        '''
        this method tests for an empty list
        '''
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())
    
    def test_save_one_rectangle(self):
        '''
        this method tests for one rectangle
        '''
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            self.assertEqual('[{"id": 32, "x": 2, "y": 8, "width": 10, "height": 7}]', f.read())

    def test_save_one_square(self):
        '''
        this method tests for one square
        '''
        s1 = Square(10, 7, 2, 8)
        Square.save_to_file([s1])
        with open("Square.json", "r") as f:
            self.assertEqual('[{"id": 8, "x": 7, "y": 2, "size": 10}]', f.read())

    def test_save_overwrite(self):
        '''
        this method tests for overwrite
        '''
        s1 = Square(10, 2, 1, 1)
        Square.save_to_file([s1])
        s2 = Square(1, 1)
        Square.save_to_file([s2])
        with open("Square.json", "r") as f:
            self.assertEqual('[{"id": 33, "x": 1, "y": 0, "size": 1}]', f.read())

    def test_save_no_args(self):
        '''
        this method tests for zero arguments
        '''
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_two_arg(self):
        '''
        this method tests for more than one arguments
        '''
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], [])