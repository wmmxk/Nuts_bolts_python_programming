import unittest
from helper.test_sort import is_alphabetized
class IsAlphabetized(unittest.TestCase):
    def test_is_alphabetized(self):
        self.assertTrue(is_alphabetized('abcd'))
