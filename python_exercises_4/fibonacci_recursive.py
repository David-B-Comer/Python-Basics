"""
Given a term (n), determine the value of x(n).
In the fibonacci_recursive.py program, create a function called fibonacci. The function should take in an integer and return the value of x(n).
This problem must be solved using recursion.
"""

import sys

def fibonacci(n):
	if n < 0:
		print("Incorrect input")
	elif n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    print('Enter a number : ')
    n = int(sys.stdin.readline())
    print(fibonacci(n))

if __name__=='__main__':
    main()