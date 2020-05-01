"""
Define a function named exponentiate with the following criteria:

Takes two integers as arguments.
Returns the value of the first integer raised to the power of the second integer.
Make sure the function has an appropriate docstring.
Define a function named raise_to_fourth_power with the following criteria:

Takes one integer as an argument.
Calls the exponentiate function to raise the given paremeter to the 4th power.
Make sure the function has an appropriate docstring.
Create a variable called square. The value assigned to this variable should be a lambda expression that utilizes the exponentiate function to raise a number to the power of 2.

Create a variable called cube. The value assigned to this variable should be a lambda expression that utilizes the exponentiate function to raise a number to the power of 3.

In the main part of your script, print the output of square(2).

In the main part of your script, print the output of cube(2).

In the main part of your script, print the output of raise_to_fourth_power(2).

When executed, your script should provide the following output.

4
8
16
"""

# x represents base number, y represents to what power the base is raised
def exponentiate(x, y):
	return x**y


def raise_to_fourth_power(x):
	return x**4


square = lambda x: exponentiate(x, 2)

cube = lambda x: exponentiate(x, 3)

print(square(2))
print(cube(2))
print(raise_to_fourth_power(2))