from fizzbuzz import fizzbuzz
import unittest

class FizzBuzzTest(unittest.TestCase):

	def setUp(self):
		self.fizzbuzz = {
			1 : 1,
			2 : 2,
			3 : "Fizz",
			4 : 4,
			5 : "Buzz",
			6 : "Fizz",
			7 : 7,
			8 : 8,
			9 : "Fizz",
			10 : "Buzz",
			11 : 11,
			12 : "Fizz",
			13 : 13,
			14 : 14,
			15 : "FizzBuzz"
		}

	def testFizzBuzz(self):
		for i in self.fizzbuzz.keys():
			self.assertEqual(self.fizzbuzz[i], fizzbuzz(i))

