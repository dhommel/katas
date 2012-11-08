require 'fizzbuzz'

describe "fizzbuzz" do
	it "should return Fizz if int is dividable by 3" do
		3.fizzbuzz.should eq "Fizz"
		6.fizzbuzz.should eq "Fizz"
		9.fizzbuzz.should eq "Fizz"
	end

	it "should return Buzz if int is dividable by 5" do
		5.fizzbuzz.should eq "Buzz"
		10.fizzbuzz.should eq "Buzz"
	end

	it "should return FizzBuzz if int dividable by 3 and 5" do
		15.fizzbuzz.should eq "FizzBuzz"
		30.fizzbuzz.should eq "FizzBuzz"
	end

	it "should return the int as string if not dividable by 3 or 5" do
		1.fizzbuzz.should eq "1"
		7.fizzbuzz.should eq "7"
	end
end
