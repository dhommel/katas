def fizzbuzz(i):
	if i % 15 == 0:
		return "FizzBuzz"
	if i % 5 == 0:
		return "Buzz"
	if i % 3 == 0:
		return "Fizz"
	return str(i)
