__author__ = 'kaniu'
from primenumber import find_primes
import unittest

class TestMyFunctions(unittest.TestCase):
	def test_it_works(self):
		self.assertEqual(find_primes(2), 2)
	def test_it_takes_int(self):
		self.assertIsInstance(find_primes(23), int)
	def test_no_negatives_allowed(self):
		self.assertRaises(find_primes(-1),ValueError)
	def test_does_not_take_floats(self):
		self.assertRaises(find_primes(1.1),TypeError)
	def test_does_not_take_string(self):
		self.assertRaises(find_primes('a'),TypeError)

if __name__ == '__main__':
	unittest.main()
