"""
Given a number (x), determine the value of x!
"""
import math
n = int(input("Enter a number to get the factorial:\n"))

def factorials():
	print("The factorial of ", n, "is ", math.factorial(n))

def main():
	factorials()

if __name__ == '__main__':
	main()
