'''
We define another function to capture the value of input
Refactor version 4 as a decorator
'''

import unittest
from helper.is_sorted import is_sorted


def make_method(input_):
    test_name = 'test_is_sorted_{}'.format(input_)
    def test_input(self):
        self.assertTrue(is_sorted(input_),u'{}  was not sorted'.format(input_))
    return test_name, test_input

def add_methods(*inputs):
    def decorator(klass):
        for input in inputs:
           test_name, test_input = make_method(input_ = input)
           setattr(klass, test_name, test_input)
        return klass
    return decorator

test_list = (
           'ab',
           'iOS',
           'A-Cert'
        )
@add_methods(*test_list)
class IsSort(unittest.TestCase):
    pass
