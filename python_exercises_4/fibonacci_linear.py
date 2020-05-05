"""
Given a term (n), determine the value of x(n).
In the fibonacci_linear.py program, create a function called fibonnaci.
The function should take in an integer and return the value of x(n).
This problem must be solved WITHOUT the use of recursion.
"""

import sys
import math

def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	elif n > 2:
		a = 1  # variable for (n - 1)
		b = 1  # variable for (n - 2)
		for x in range(3, n + 1):
			c = a + b
			a, b = b, c

		return c

def main():
    print('Enter a number : ')
    n = int(sys.stdin.readline())
    print(fibonacci(n))

if __name__=='__main__':
    main()