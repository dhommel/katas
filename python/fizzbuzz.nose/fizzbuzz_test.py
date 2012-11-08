from hamcrest import *
from fizzbuzz import fizzbuzz

data = {
	1 : "1",
	2 : "2",
	3 : "Fizz",
	4 : "4",
	5 : "Buzz",
	6 : "Fizz",
	7 : "7",
	8 : "8",
	9 : "Fizz",
	10 : "Buzz",
	11 : "11",
	12 : "Fizz",
	13 : "13",
	14 : "14",
	15 : "FizzBuzz",
}

def check_values(i, s):
	assert_that(fizzbuzz(i), equal_to(s))

def test_fizzbuzz():
	for i in data.keys():
		yield check_values, i, data[i]
