#!/usr/bin/python3
'''
this module contains test cases
for the class Base. It test the init
to json and from json methods
'''
import unittest
from models.base_abel import Base


class TestBase(unittest.TestCase):
    '''
    this is the class with all the test case methods
    '''
    def test_init(self):
        '''
        this tests the init method
        '''
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        b4 = Base()
        self.assertEqual(b4.id, 3)

        b5 = Base(-5)
        self.assertEqual(b5.id, -5)

        b6 = Base(6.3)
        self.assertEqual(b6.id, 6.3)

        b7 = Base(None)
        self.assertEqual(b7.id, 4)

    def test_to_json_string(self):
        '''
        this tests the to json method
        '''
        c1 = Base()
        c_dict = c1.to_dictionary()
        json_dict = Base.to_json_string([c_dict])
        json_dict2 = Base.to_json_string(None)
        self.assertEqual(json_dict, '[{"id": 5}]')
        self.assertEqual(json_dict2, '[]')

    def test_from_json_string(self):
        '''
        this method tests the from json method
        '''
        json_dict = '[{"id": 1}]'
        list_dicts = Base.from_json_string(json_dict)
        list_dicts2 = Base.from_json_string(None)
        self.assertEqual(list_dicts, [{"id": 1}])
        self.assertEqual(list_dicts2, [])
