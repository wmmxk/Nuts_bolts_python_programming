'''
You tried to test a list of cases, the testing stops at the first failure

'''

import unittest
from helper.is_sorted import is_sorted

class IsSort(unittest.TestCase):
    def test_is_sorted(self):
        inputs = [
                '',
                'a',
                'aaa',
                'abcd',
                'iOS',
                'A-Cert'
                ]
        for input in inputs:
            self.assertTrue(is_sorted(input),u'{} was not sorted'.format(input))
