"""
The program must meet the following criteria.
A function that asks the user to provide a number between 0 and 10.
A function that returns a random number between 1 and 10.
A function that evaluates the randomly generated number against the user's guess.
At the end, the program must output the following:
The random number that was generated.
The user's guess.
An indication if the user guess correctly or if the user's guess was too high/too low.
"""
from random import randrange


def guess_a_number():


	guess = int(input("Select a number between 0 and 10"))
	print("User selection was : " + str(guess))

	random_number1to10 = int((randrange(1, 10)))
	print("The random number was : " + str(random_number1to10))

	if guess == random_number1to10:
		print("You guessed correctly!")

	elif guess > random_number1to10:
		print("You guessed too high")

	else:
		print("You guessed too low")

guess_a_number()




