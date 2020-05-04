"""
The program should meet the following criteria:
	The program prints each number from 1 to 100 to a new line.
	If the number is a multiple of 3, print "Fizz" instead of the number.
	If the number is a multiple of 5, print "Buzz" instead of the number.
	If the number is a multiple of both 3 and 5, print "FizzBuzz" instead of the number.
"""


def main():
	for fizzbuzz in range(101):
		if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
			print("fizzbuzz")
			continue
		elif fizzbuzz % 3 == 0:
			print("fizz")
			continue
		elif fizzbuzz % 5 == 0:
			print("buzz")
			continue
		print(fizzbuzz)

if __name__ == '__main__':
    main()