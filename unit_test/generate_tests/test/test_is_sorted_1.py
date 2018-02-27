import unittest
from helper.is_sorted import is_sorted

class IsSorted(unittest.TestCase):
    def test_is_sorted(self):
        self.assertTrue(is_sorted('abcd'))

    def test_is_not_sorted(self):
        self.assertFalse(is_sorted('adc'))
