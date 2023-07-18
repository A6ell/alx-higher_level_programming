#!/usr/bin/python3
'''
this module contains tests
for the create function of
the Base class
'''
import unittest
from models.base_abel import Base
from models.rectangle_abel import Rectangle
from models.square_abel import Square


class Test_Create(unittest.TestCase):
    '''
    class test of the create base function
    '''

    def test_rectangle_create(self):
        '''
        for rectangle
        '''
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_square_create(self):
        '''
        for square
        '''
        r1 = Square(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)
