'''
We define another function to capture the value of input
'''

import unittest
from helper.is_sorted import is_sorted

class IsSort(unittest.TestCase):
    pass

def make_method(input_):
    test_name = 'test_is_sorted_{}'.format(input_)
    def test_input(self):
        self.assertTrue(is_sorted(input_),u'{}  was not sorted'.format(input_))
    return test_name, test_input

def add_methods(klass, *inputs):
    for input in inputs:
        test_name, test_input = make_method(input_ = input)
        setattr(klass, test_name, test_input)

test_list = (
           'ab',
           'iOS',
           'A-Cert'
        )
add_methods(IsSort,*test_list)
