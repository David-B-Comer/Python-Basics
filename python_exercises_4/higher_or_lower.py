"""
Create a copy of the program called higher_or_lower.py from exercise 2 in Part 3.
Extend the functionality to meet the following requirements:
If a user's guess is incorrect, they get to keep guessing until they get it right.
"""

from random import randrange


def guess_a_number():

	guess = 0
	random_number1to10 = int((randrange(1, 10)))

	while guess != random_number1to10:
		guess = int(input("Select a number between 0 and 10\n"))
		print("User selection was : " + str(guess))
		if (guess > random_number1to10):
			print("You guessed too high")
		if (guess < random_number1to10):
			print("You guessed too low")
	print("You guessed correctly!")

def main():
	guess_a_number()

if __name__=='__main__':
    main()
