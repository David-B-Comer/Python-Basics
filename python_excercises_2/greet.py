"""
Define a function called greet that meets the following criteria:
Takes an argument called name.
Prints a greeting using the name parameter.
Define another function called name_input that meets the following criteria:
Takes no arguments.
Prints a message to the screen requesting the user to provide a name.
Returns a string with the value equals to that of the provided name.
Using these two functions, prompt the user for a name and print it to the screen.
Each function must have an appropriate docstring.
"""

# get name input with prompt and prints greeting with name
def name_input():
    global name
    name = input("Please enter your name")
# print greeting
def greet():
    print("Hello " + name + "!")


name_input()
greet()