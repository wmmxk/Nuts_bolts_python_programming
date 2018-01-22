import unittest
from helper.test_prime import is_prime

class IsPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(5))
