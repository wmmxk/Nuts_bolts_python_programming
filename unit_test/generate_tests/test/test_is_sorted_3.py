'''
You define a function, add_method, to create a method for each test case and add it the klass you defined uisng setattr

Due to scope issue, it does not work, the input is always the last one

'''

import unittest
from helper.is_sorted import is_sorted

class IsSort(unittest.TestCase):
    pass

def add_methods(klass, *inputs):
    for input in inputs:
        test_name = 'test_is_sorted_{}'.format(input)
        def test_input(self):
            self.assertTrue(is_sorted(input), u'{} was not sorted'.format(input))
        setattr(klass, test_name, test_input)

test_list = (
           'ab',
           'iOS',
           'A-Cert'
        )
add_methods(IsSort,*test_list)
