from primes import primesOf
import unittest

class PrimesTest(unittest.TestCase):

	def setUp(self):
		self.primes = {
			1 : [],
			2 : [2],
			3 : [3],
			4 : [2, 2],
			5 : [5],
			6 : [2, 3],
			7 : [7],
			8 : [2, 2, 2],
			9 : [3, 3],
			2 * 3 * 5 * 7 * 11 * 13 : [2, 3, 5, 7, 11, 13],
		}
	
	def testPrimesOf(self):
		for i in self.primes.keys():
			self.assertEqual(self.primes[i], primesOf(i))

