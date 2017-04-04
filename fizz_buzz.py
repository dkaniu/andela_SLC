__author__ = 'kaniu'

def fizz_buzz(test_fizz_argument):
	selector = {
      test_fizz_argument % 3 == 0 and test_fizz_argument % 5 == 0: "FizzBuzz",
      test_fizz_argument % 5 == 0: "Buzz",
      test_fizz_argument % 3 == 0: "Fizz"
    }
	return selector.get(test_fizz_argument, test_fizz_argument)
